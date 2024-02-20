#!/bin/bash

# Run Tableau backup command
tsm maintenance backup -d

# Move backup file to S3 bucket
aws s3 cp /var/opt/tableau/tableau_server/data/tabsvc/files/backups/*.tsbak s3://gbt-tableaubucket/

# Remove old backup files
# Example: Remove files older than 7 days
find /var/opt/tableau/tableau_server/data/tabsvc/files/backups/ -type f -name "*.tsbak" -mtime +7 -exec rm {} \;
