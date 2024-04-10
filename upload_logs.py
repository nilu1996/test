Response
{
  "errorMessage": "An error occurred (ValidationException) when calling the DescribeApp operation: Either UserProfileName or SpaceName must be passed for DescribeApp operation.",
  "errorType": "ClientError",
  "stackTrace": [
    "  File \"/var/task/index.py\", line 16, in lambda_handler\n    activity_status = sagemaker_client.describe_app(\n",
    "  File \"/var/runtime/botocore/client.py\", line 553, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n",
    "  File \"/var/runtime/botocore/client.py\", line 1009, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"
  ]
}
