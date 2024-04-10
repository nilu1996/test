import boto3
import time

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
        activity_status = sagemaker_client.describe_app(
            AppName=app_name,
            AppType=app_type,
            DomainId=app_domain
        )
        print(activity_status)
        if activity_status['App']['Status'] == 'Stopped':
            print(f'Studio Lab instance "{app_name}" is already stopped.')
        else:
            last_activity_timestamp = activity_status['App']['LastHealthCheckTimestamp']
            current_time = int(time.time())
            idle_time = current_time - last_activity_timestamp
            if idle_time >= IDLE_THRESHOLD_SECONDS:
                sagemaker_client.stop_app(AppName=app_name)
                print(f'Stopped Studio Lab instance "{app_name}" due to inactivity.')
            else:
                print(f'Studio Lab instance "{app_name}" is active, not yet past the idle threshold.')
    return {'statusCode': 200, 'body': 'Success'}
