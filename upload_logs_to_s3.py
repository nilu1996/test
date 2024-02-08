 0 8 * * * /bin/python2.7 /home/tsmadmin/scripts/upload_s3_logs.py

0 8 * * * /bin/python2.7 /home/tsmadmin/scripts/upload_s3_logs.py >> /home/tsmadmin/scripts/cron_log.txt 2>&1

s3://gbt-tableaubucket/logs/_var_opt_tableau_tableau_server_data_tabsvc_logs_httpd/



