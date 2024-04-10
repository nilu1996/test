{'AppArn': 'arn:aws:sagemaker:us-east-1:787098058239:app/d-ushbqegfkcgl/jupytertest/jupyterlab/default', 'AppType': 'JupyterLab', 'AppName': 'default', 'DomainId': 'd-ushbqegfkcgl', 'SpaceName': 'jupytertest', 'Status': 'InService', 'LastHealthCheckTimestamp': datetime.datetime(2024, 4, 10, 8, 7, 52, 973000, tzinfo=tzlocal()), 'LastUserActivityTimestamp': datetime.datetime(2024, 4, 10, 8, 7, 52, 973000, tzinfo=tzlocal()), 'CreationTime': datetime.datetime(2024, 4, 10, 7, 8, 57, 58000, tzinfo=tzlocal()), 'ResourceSpec': {'SageMakerImageArn': 'arn:aws:sagemaker:us-east-1:885854791233:image/sagemaker-distribution-cpu', 'SageMakerImageVersionAlias': '1.6.0', 'InstanceType': 'ml.t3.medium'}, 'ResponseMetadata': {'RequestId': '0fe59209-9f29-484b-b24c-cd537b22abe0', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '0fe59209-9f29-484b-b24c-cd537b22abe0', 'content-type': 'application/x-amz-json-1.1', 'content-length': '645', 'date': 'Wed, 10 Apr 2024 08:08:29 GMT'}, 'RetryAttempts': 0}}


activity_status = sagemaker_client.describe_app(
            AppName=app_name,
            AppType=app_type,
            DomainId=app_domain,
            SpaceName=app_attribute  # Use the determined attribute
        )
