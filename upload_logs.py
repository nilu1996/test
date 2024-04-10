import boto3
import time
from datetime import datetime

sagemaker_client = boto3.client('sagemaker')

IDLE_THRESHOLD_SECONDS = 300  # 5 minutes

def lambda_handler(event, context):
    response = sagemaker_client.list_apps()
    print(response)
    for app in response['Apps']:
        app_name = app['AppName']
        app_type = app['AppType']
        app_domain = app['DomainId']
        print(app_name)
        
        # Determine which attribute to use based on application type
        if app_type == 'JupyterLab':
            app_attribute = app['SpaceName']
        elif app_type == 'JupyterServer':
            app_attribute = app['UserProfileName']
        else:
            print(f"Unsupported application type: {app_type}")
            continue
        
        activity_status = sagemaker_client.describe_app(
            AppName=app_name,
            AppType=app_type,
            DomainId=app_domain,
            SpaceName=app_attribute  # Use the determined attribute
        )
        print(activity_status)
        if activity_status['Status'] == 'InService':
            last_activity_timestamp = activity_status['LastHealthCheckTimestamp']
            current_time = int(time.time())
            last_activity_timestamp_unix = int(last_activity_timestamp.timestamp())  # Convert to Unix timestamp
            running_time = current_time - last_activity_timestamp_unix  # Calculate running time
            if running_time >= IDLE_THRESHOLD_SECONDS:
                sagemaker_client.stop_app(AppName=app_name)
                print(f'Stopped Studio Lab instance "{app_name}" due to running for more than 5 minutes.')
            else:
                print(f'Studio Lab instance "{app_name}" is still running, not yet past the 5-minute threshold.')
        else:
            print(f'Studio Lab instance "{app_name}" is not in service.')
    return {'statusCode': 200, 'body': 'Success'}
