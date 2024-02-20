
Error 
/usr/bin/python3.8: can't open file '/home/svc_calinuser177/health_notificatio_scripts/web_monitory.py': [Errno 2] No such file or directory

I am using python 3.8

This cron exprecssion

*/30 * * * * /usr/bin/python3.8 /home/svc_calinuser177/health_notificatio_scripts/web_monitory.py >> /home/svc_calinuser177/health_notificatio_scripts/log_file.log 2>&1
