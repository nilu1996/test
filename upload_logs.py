{
  "errorMessage": "An error occurred (ValidationException) when calling the DescribeApp operation: Either UserProfileName or SpaceName must be passed for DescribeApp operation.",
  "errorType": "ClientError",
  "stackTrace": [
    "  File \"/var/task/index.py\", line 16, in lambda_handler\n    activity_status = sagemaker_client.describe_app(\n",
    "  File \"/var/runtime/botocore/client.py\", line 553, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n",
    "  File \"/var/runtime/botocore/client.py\", line 1009, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"
  ]
}

Function Logs
START RequestId: 389990e3-896d-455e-9033-cf38ac7bb9bb Version: $LATEST
{'Apps': [{'DomainId': 'd-ushbqegfkcgl', 'SpaceName': 'jupytertest', 'AppType': 'JupyterLab', 'AppName': 'default', 'Status': 'InService', 'CreationTime': datetime.datetime(2024, 4, 10, 7, 8, 57, 58000, tzinfo=tzlocal()), 'ResourceSpec': {'SageMakerImageArn': 'arn:aws:sagemaker:us-east-1:885854791233:image/sagemaker-distribution-cpu', 'SageMakerImageVersionAlias': '1.6.0', 'InstanceType': 'ml.t3.medium'}}, {'DomainId': 'd-jxc4qqbqwy0a', 'UserProfileName': 'default-1687560300049', 'AppType': 'JupyterServer', 'AppName': 'default', 'Status': 'InService', 'CreationTime': datetime.datetime(2023, 8, 25, 14, 58, 24, 594000, tzinfo=tzlocal()), 'ResourceSpec': {'SageMakerImageArn': 'arn:aws:ecr:us-east-1:081325390199:repository/looseleaf-jupyter-server-3', 'InstanceType': 'system'}}], 'ResponseMetadata': {'RequestId': '4c14297f-7e34-4074-ad30-4fa671bc173f', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '4c14297f-7e34-4074-ad30-4fa671bc173f', 'content-type': 'application/x-amz-json-1.1', 'content-length': '834', 'date': 'Wed, 10 Apr 2024 08:04:04 GMT'}, 'RetryAttempts': 0}}
default
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] ClientError: An error occurred (ValidationException) when calling the DescribeApp operation: Either UserProfileName or SpaceName must be passed for DescribeApp operation.
Traceback (most recent call last):
  File "/var/task/index.py", line 16, in lambda_handler
    activity_status = sagemaker_client.describe_app(
  File "/var/runtime/botocore/client.py", line 553, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/var/runtime/botocore/client.py", line 1009, in _make_api_call
    raise error_class(parsed_response, operation_name)END RequestId: 389990e3-896d-455e-9033-cf38ac7bb9bb
REPORT RequestId: 389990e3-896d-455e-9033-cf38ac7bb9bb	Duration: 466.14 ms	Billed Duration: 467 ms	Memory Size: 128 MB	Max Memory Used: 80 MB	Init Duration: 496.49 ms

Request ID
389990e3-896d-455e-9033-cf38ac7bb9bb
