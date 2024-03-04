  warnings.warn(warning, PythonDeprecationWarning)
Traceback (most recent call last):
  File "backyp.py", line 62, in <module>
    Message="Tableau UAT Server backup failed. Backup file {} not found in {}".format(backup_file, BACKUP_DIR)
  File "/usr/lib/python2.7/site-packages/botocore/client.py", line 386, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/usr/lib/python2.7/site-packages/botocore/client.py", line 692, in _make_api_call
    operation_model, request_dict, request_context)
  File "/usr/lib/python2.7/site-packages/botocore/client.py", line 711, in _make_request
    return self._endpoint.make_request(operation_model, request_dict)
  File "/usr/lib/python2.7/site-packages/botocore/endpoint.py", line 102, in make_request
    return self._send_request(request_dict, operation_model)
  File "/usr/lib/python2.7/site-packages/botocore/endpoint.py", line 137, in _send_request
    success_response, exception):
  File "/usr/lib/python2.7/site-packages/botocore/endpoint.py", line 256, in _needs_retry
    caught_exception=caught_exception, request_dict=request_dict)
  File "/usr/lib/python2.7/site-packages/botocore/hooks.py", line 356, in emit
    return self._emitter.emit(aliased_event_name, **kwargs)
  File "/usr/lib/python2.7/site-packages/botocore/hooks.py", line 228, in emit
    return self._emit(event_name, kwargs)
  File "/usr/lib/python2.7/site-packages/botocore/hooks.py", line 211, in _emit
    response = handler(**kwargs)
  File "/usr/lib/python2.7/site-packages/botocore/retryhandler.py", line 183, in __call__
    if self._checker(attempts, response, caught_exception):
  File "/usr/lib/python2.7/site-packages/botocore/retryhandler.py", line 251, in __call__
    caught_exception)
  File "/usr/lib/python2.7/site-packages/botocore/retryhandler.py", line 277, in _should_retry
    return self._checker(attempt_number, response, caught_exception)
  File "/usr/lib/python2.7/site-packages/botocore/retryhandler.py", line 317, in __call__
    caught_exception)
  File "/usr/lib/python2.7/site-packages/botocore/retryhandler.py", line 223, in __call__
    attempt_number, caught_exception)
  File "/usr/lib/python2.7/site-packages/botocore/retryhandler.py", line 359, in _check_caught_exception
    raise caught_exception
botocore.exceptions.SSLError: SSL validation failed for https://sns.us-east-1.amazonaws.com/ [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)
