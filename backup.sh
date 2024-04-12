Script is looking for tsm when running from cron tab and its getting failed due to that
TSM loccation: /opt/tableau/tableau_server/packages/customer-bin.20233.23.1017.0948/tsm

Keep script same change tsm backup command setting

BACKUP_DIR="/var/opt/tableau/tableau_server/data/tabsvc/files/backups/"
S3_BUCKET="s3://gbt-uattableau/backup/"
SNS_ARN="arn:aws:sns:us-east-1:090124397890:Instance-Health-monitoring"
EMAIL_SUBJECT="Tableau Server Backup Notification"

# Run Tableau backup command
tsm maintenance backup -f backup.tsbak -d

# Remove backup files older than 2 days
find "$BACKUP_DIR" -maxdepth 1 -type f -name "*.tsbak" -mtime +2 -exec rm {} \;

# Move latest backup file to S3 bucket
latest_backup=$(ls -t "$BACKUP_DIR" | head -1)
if [ -n "$latest_backup" ]; then
    aws s3 cp "${BACKUP_DIR}${latest_backup}" "$S3_BUCKET" --no-verify-ssl

    # Send success notification
    aws sns publish --topic-arn "$SNS_ARN" --subject "$EMAIL_SUBJECT" --message "Tableau UAT Server backup completed successfully." --no-verify-ssl
else
    # Send failure notification if no backup files are found
    aws sns publish --topic-arn "$SNS_ARN" --subject "$EMAIL_SUBJECT" --message "Tableau UAT Server backup failed. No backup files found in $BACKUP_DIR" --no-verify-ssl
fi
