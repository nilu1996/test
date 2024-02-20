#!/bin/bash

# Define paths
BACKUP_DIR="/var/opt/tableau/tableau_server/data/tabsvc/files/backups/"
S3_BUCKET="s3://gbt-tableaubucket/backup/"

# Run Tableau backup command
tsm maintenance backup -d

# Check if backup files exist
if [ -n "$(find "$BACKUP_DIR" -maxdepth 1 -type f -name "*.tsbak" -print -quit)" ]; then
    # Move backup file to S3 bucket
    aws s3 cp "$BACKUP_DIR"*.tsbak "$S3_BUCKET"
    # Remove old backup files
    # Example: Remove files older than 7 days
    find "$BACKUP_DIR" -maxdepth 1 -type f -name "*.tsbak" -mtime +7 -exec rm {} \;
else
    echo "No backup files found in $BACKUP_DIR"
fi
