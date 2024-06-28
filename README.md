Link : https://docs.infotopics.com/mailscheduler/installation-guide/upgrade


Mail Sceduler : 3.0.2  latest : 3.1.0

1. downlaod latest file from mailscheduler website link
    https://docs.infotopics.com/mailscheduler/installation-guide/upgrade

2. Upload that file to give tableau extetion driver path.

3. Stop the mailscheduler-amd64 service
   ./mailscheduler-amd64 service stop

3. Rename old file 
   mv mailscheduler-amd64 mailscheduler-amd64-old
   
4. Place new file in same location
   /home/svc_calinuser177/tableau_infotopics
   
   aws s3 cp s3://gbt-tableau/mailscheduler-amd64 .

5. Make Mailsceduler file excutable 
   chmod +x mailscheduler-amd64

6. Start the mailscheduler serice 
   mailscheduler-amd64 service start 
