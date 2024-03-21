import requests
from datetime import datetime
import getopt
import sys
import boto3
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Usage
usageInfo = """Usage:
This script checks if a notebook is idle for X seconds and stops it:
python autostop.py --time <time_in_seconds> [--port <jupyter_port>] [--ignore-connections] [--region <aws_region>]
Type "python autostop.py -h" for available options.
"""
# Help info
helpInfo = """-t, --time
    Auto stop time in seconds
-p, --port
    Jupyter port
-c --ignore-connections
    Stop notebook once idle, ignore connected users
-h, --help
    Help information
--region
    AWS region
"""

# Read command-line parameters
idle = True
port = '8888'
ignore_connections = False
region = 'us-east-1'  # Default AWS region
try:
    opts, args = getopt.getopt(sys.argv[1:], "ht:p:c", ["help", "time=", "port=", "ignore-connections", "region="])
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
        if opt in ("--region"):
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
    last_activity = datetime.strptime(last_activity, "%Y-%m-%dT%H:%M:%S.%fz")
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

# This is hitting Jupyter's sessions API
try:
    response = requests.get(f'https://default:{port}/jupyterlab/default/api/sessions', verify=True, timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error occurred while connecting to Jupyter sessions API:", e)
    exit(1)

print(response)
data = response.json()

if len(data) > 0:
    for notebook in data:
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
    print("No active sessions detected. Checking Studio app details.")
    client = boto3.client('sagemaker', region_name=region)
    DomainId, SpaceName, AppType, AppName = get_studio_app_details()
    uptime = client.describe_app(
        DomainId=DomainId,
        SpaceName=SpaceName,
        AppType=AppType,
        AppName=AppName
    )['LastUserActivityTimestamp']
    if not is_idle(uptime.strftime("%Y-%m-%dT%H:%M:%S.%fz")):
        idle = False

if idle:
    print('Closing idle notebook')
    print('shutting down NB')
    client = boto3.client('sagemaker', region_name=region)
    DomainId, SpaceName, AppType, AppName = get_studio_app_details()
    print(DomainId, AppType, AppName, SpaceName)
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
