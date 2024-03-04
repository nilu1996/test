Traceback (most recent call last):
  File "backup.py", line 56, in <module>
    sns_client = boto3.client("sns")
  File "/usr/lib/python2.7/site-packages/boto3/__init__.py", line 93, in client
    return _get_default_session().client(*args, **kwargs)
  File "/usr/lib/python2.7/site-packages/boto3/session.py", line 263, in client
    aws_session_token=aws_session_token, config=config)
  File "/usr/lib/python2.7/site-packages/botocore/session.py", line 851, in create_client
    client_config=config, api_version=api_version)
  File "/usr/lib/python2.7/site-packages/botocore/client.py", line 88, in create_client
    verify, credentials, scoped_config, client_config, endpoint_bridge)
  File "/usr/lib/python2.7/site-packages/botocore/client.py", line 357, in _get_client_args
    verify, credentials, scoped_config, client_config, endpoint_bridge)
  File "/usr/lib/python2.7/site-packages/botocore/args.py", line 73, in get_client_args
    endpoint_url, is_secure, scoped_config)
  File "/usr/lib/python2.7/site-packages/botocore/args.py", line 154, in compute_client_args
    s3_config=s3_config,
  File "/usr/lib/python2.7/site-packages/botocore/args.py", line 220, in _compute_endpoint_config
    return self._resolve_endpoint(**resolve_endpoint_kwargs)
  File "/usr/lib/python2.7/site-packages/botocore/args.py", line 303, in _resolve_endpoint
    service_name, region_name, endpoint_url, is_secure)
  File "/usr/lib/python2.7/site-packages/botocore/client.py", line 431, in resolve
    service_name, region_name)
  File "/usr/lib/python2.7/site-packages/botocore/regions.py", line 134, in construct_endpoint
    partition, service_name, region_name)
  File "/usr/lib/python2.7/site-packages/botocore/regions.py", line 148, in _endpoint_for_partition
    raise NoRegionError()
botocore.exceptions.NoRegionError: You must specify a region.
