Traceback (most recent call last):
  File "web_monitory.py", line 27, in <module>
    check_website_availability(website_url, sns_topic_arn)
  File "web_monitory.py", line 21, in check_website_availability
    send_sns_notification(sns_topic_arn, message)
  File "web_monitory.py", line 6, in send_sns_notification
    sns_client = boto3.client('sns')
  File "/usr/local/lib/python3.8/site-packages/boto3/__init__.py", line 92, in client
    return _get_default_session().client(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/boto3/session.py", line 299, in client
    return self._session.create_client(
  File "/usr/local/lib/python3.8/site-packages/botocore/session.py", line 997, in create_client
    client = client_creator.create_client(
  File "/usr/local/lib/python3.8/site-packages/botocore/client.py", line 161, in create_client
    client_args = self._get_client_args(
  File "/usr/local/lib/python3.8/site-packages/botocore/client.py", line 508, in _get_client_args
    return args_creator.get_client_args(
  File "/usr/local/lib/python3.8/site-packages/botocore/args.py", line 100, in get_client_args
    final_args = self.compute_client_args(
  File "/usr/local/lib/python3.8/site-packages/botocore/args.py", line 219, in compute_client_args
    endpoint_config = self._compute_endpoint_config(
  File "/usr/local/lib/python3.8/site-packages/botocore/args.py", line 369, in _compute_endpoint_config
    return self._resolve_endpoint(**resolve_endpoint_kwargs)
  File "/usr/local/lib/python3.8/site-packages/botocore/args.py", line 474, in _resolve_endpoint
    return endpoint_bridge.resolve(
  File "/usr/local/lib/python3.8/site-packages/botocore/client.py", line 613, in resolve
    resolved = self.endpoint_resolver.construct_endpoint(
  File "/usr/local/lib/python3.8/site-packages/botocore/regions.py", line 229, in construct_endpoint
    result = self._endpoint_for_partition(
  File "/usr/local/lib/python3.8/site-packages/botocore/regions.py", line 277, in _endpoint_for_partition
    raise NoRegionError()
botocore.exceptions.NoRegionError: You must specify a region.
