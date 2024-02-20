tsm maintenance backup -f backup.tsbak -d

This command is used to generate backup files in tableau server 

And its saves in defaaul location 

/var/opt/tableau/tableau_server/data/tabsvc/files/backups/<filename>.tsbak

I wanted to automation in server only using that I can take backup on every friday 1AM MST and store that backup s3 bucket.

Remove old backup file from location
