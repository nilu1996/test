#!/bin/bash

# Define paths
BACKUP_DIR="/var/opt/tableau/tableau_server/data/tabsvc/files/backups/"
S3_BUCKET="s3://gbt-uattableau/backup/"

# Copy files to S3 bucket
aws s3 cp "$BACKUP_DIR" "$S3_BUCKET" --recursive --no-verify-ssl
