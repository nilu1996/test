No old logs found in /var/opt/tableau/tableau_server/data/tabsvc/logs/httpd.
Traceback (most recent call last):
  File "upload_s3.py", line 70, in <module>
    old_logs = collect_logs_older_than_seven_days(local_logs_path)
  File "upload_s3.py", line 47, in collect_logs_older_than_seven_days
    for file_name in os.listdir(logs_dir):
OSError: [Errno 20] Not a directory: '/var/opt/tableau/tableau_server/data/tabsvc/logs/httpd.zip'
