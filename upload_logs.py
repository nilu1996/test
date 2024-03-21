#     Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#     Licensed under the Apache License, Version 2.0 (the "License").
#     You may not use this file except in compliance with the License.
#     A copy of the License is located at
#
#         https://aws.amazon.com/apache-2-0/
#
#     or in the "license" file accompanying this file. This file is distributed
#     on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
#     express or implied. See the License for the specific language governing
#     permissions and limitations under the License.

import requests
from datetime import datetime
import getopt, sys
import urllib3
import boto3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Usage
usageInfo = """Usage:
This scripts checks if a notebook is idle for X seconds if it does, it'll stop the notebook:
python autostop.py --time <time_in_seconds> [--port <jupyter_port>] [--ignore-connections]
Type "python autostop.py -h" for available options.
"""
# Help info
helpInfo = """-t, --time
    Auto stop time in seconds
-p, --port
    jupyter port
-c --ignore-connections
    Stop notebook once idle, ignore connected users
-h, --help
    Help information
"""

# Read in command-line parameters
idle = True
port = '8888'
ignore_connections = False
try:
    opts, args = getopt.getopt(sys.argv[1:], "ht:p:c", ["help","time=","port=","ignore-connections", "region="]) # Add "region=" to the list of options
    if len(opts) == 0:
        raise getopt.GetoptError("No input parameters!")
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(helpInfo)
            exit(0)
        if opt in ("-t", "--time"):
            time = int(arg)
        if opt in ("-p", "--port"):
            port = str(arg)
        if opt in ("-c", "--ignore-connections"):
            ignore_connections = True
        if opt in ("--region"):  # Handle the new "region" option
            region = str(arg)
except getopt.GetoptError:
    print(usageInfo)
    exit(1)

# Missing configuration notification
missingConfiguration = False
if not time:
    print("Missing '-t' or '--time'")
    missingConfiguration = True
if missingConfiguration:
    exit(2)


def is_idle(last_activity):
    last_activity = datetime.strptime(last_activity,"%Y-%m-%dT%H:%M:%S.%fz")
    if (datetime.now() - last_activity).total_seconds() > time:
        print('Notebook is idle. Last activity time = ', last_activity)
        return True
    else:
        print('Notebook is not idle. Last activity time = ', last_activity)
        return False
        
def get_studio_app_details():
    metadata = '/opt/ml/metadata/resource-metadata.json'
    with open(metadata, 'r') as metdata:
        _conf = json.load(metdata)
    return _conf["DomainId"], _conf["SpaceName"],_conf["AppType"],_conf["ResourceName"]
    
def get_notebook_name():
    log_path = '/opt/ml/metadata/resource-metadata.json'
    with open(log_path, 'r') as logs:
        _logs = json.load(logs)
    return _logs['ResourceName']
    
print("I am here")

## path for new Jupyter Lab 
prefix="/jupyterlab/default"

# This is hitting Jupyter's sessions API: https://github.com/jupyter/jupyter/wiki/Jupyter-Notebook-Server-API#Sessions-API
response = requests.get('http://default:'+port+prefix+'/api/sessions', verify=False)
print(response)
data = response.json()
if len(data) > 0:
    for notebook in data:
        # Idleness is defined by Jupyter
        # https://github.com/jupyter/notebook/issues/4634
        if notebook['kernel']['execution_state'] == 'idle':
            if not ignore_connections:
                if notebook['kernel']['connections'] == 0:
                    if not is_idle(notebook['kernel']['last_activity']):
                        idle = False
                else:
                    idle = False
                    print('Notebook idle state set as %s because no kernel has been detected.' % idle)
            else:
                if not is_idle(notebook['kernel']['last_activity']):
                    idle = False
                    print('Notebook idle state set as %s since kernel connections are ignored.' % idle)
        else:
            print('Notebook is not idle:', notebook['kernel']['execution_state'])
            idle = False
else:
    print("here")
    client = boto3.client('sagemaker',region_name=region)
    DomainId,SpaceName,AppType,AppName=get_studio_app_details()
    uptime = client.describe_app(
    DomainId=DomainId,
    #UserProfileName='string',
    AppType=AppType, #'JupyterServer'|'KernelGateway'|'TensorBoard'|'RStudioServerPro'|'RSessionGateway'|'JupyterLab'|'CodeEditor',
    AppName=AppName,
    SpaceName=SpaceName
)['LastUserActivityTimestamp']

    if not is_idle(uptime.strftime("%Y-%m-%dT%H:%M:%S.%fz")):
        idle = False
        print('Notebook idle state set as %s since no sessions detected.' % idle)

if idle:
    print('Closing idle notebook')
    print('shutting down NB')
    client = boto3.client('sagemaker',region_name=region)
    DomainId,SpaceName,AppType,AppName=get_studio_app_details()
    print(DomainId,AppType,AppName,SpaceName)
    response = client.delete_app(
    DomainId=DomainId,
    SpaceName=SpaceName,
    AppType=AppType,
    AppName=AppName,

)
    print(response)
    print('shutting down NB')
    
else:
    print('Notebook not idle. Pass.')
