aws s3 cp "DRIVE:\BACKUP_FOLDER" s3://YOUR_BUCKET_NAME/backup_%date:~-4%%date:~4,2%%date:~7,2%/ --recursive
