#!/bin/bash

# Define paths
BACKUP_DIR="/var/opt/tableau/tableau_server/data/tabsvc/files/backups/"
S3_BUCKET="s3://gbt-uattableau/backup/"
SNS_ARN="arn:aws:sns:us-east-1:090124397890:Instance-Health-monitoring"
EMAIL_SUBJECT="Tableau Server Backup Notification"

# Run Tableau backup command
tsm maintenance backup -f backup.tsbak -d

# Check if backup files exist
if [ -n "$(find "$BACKUP_DIR" -maxdepth 1 -type f -name "*.tsbak" -print -quit)" ]; then
    # Move backup file to S3 bucket
    aws s3 cp "$BACKUP_DIR"*.tsbak "$S3_BUCKET" --no-verify-ssl
    # Remove old backup files    # Example: Remove files older than 7 days
    find "$BACKUP_DIR" -maxdepth 1 -type f -name "*.tsbak" -mtime +7 -exec rm {} \;

    # Send success notification
    aws sns publish --topic-arn "$SNS_ARN" --subject "$EMAIL_SUBJECT" --message "Tableau UAT Server backup completed successfully." --no-verify-ssl
else
    # Send failure notification
    aws sns publish --topic-arn "$SNS_ARN" --subject "$EMAIL_SUBJECT" --message "Tableau UAT Server backup failed. No backup files found in $BACKUP_DIR" --no-verify-ssl
fi
