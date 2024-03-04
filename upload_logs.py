Traceback (most recent call last):
  File "back.py", line 58, in <module>
    sns_client = boto3.client("sns", config=botocore.config.Config(verify=False))  # Disable SSL verification
  File "/usr/lib/python2.7/site-packages/botocore/config.py", line 193, in __init__
    args, kwargs)
  File "/usr/lib/python2.7/site-packages/botocore/config.py", line 220, in _record_user_provided_options
    'Got unexpected keyword argument \'%s\'' % key)
TypeError: Got unexpected keyword argument 'verify'
