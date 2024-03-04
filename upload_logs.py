import os
import subprocess
import datetime
import boto3

# Define paths
BACKUP_DIR = "/var/opt/tableau/tableau_server/data/tabsvc/files/backups/"
S3_BUCKET = "gbt-uattableau"
S3_PREFIX = "backup/"
SNS_ARN = "arn:aws:sns:us-east-1:090124397890:Instance-Health-monitoring"
EMAIL_SUBJECT = "Tableau Server Backup Notification"

# Run Tableau backup command
backup_file = "backup.tsbak"
subprocess.run(["tsm", "maintenance", "backup", "-f", backup_file, "-d"], cwd=BACKUP_DIR)

# Check if backup file exists
if os.path.isfile(os.path.join(BACKUP_DIR, backup_file)):
    # Move backup file to S3 bucket
    s3_client = boto3.client("s3")
    s3_key = S3_PREFIX + backup_file
    s3_client.upload_file(os.path.join(BACKUP_DIR, backup_file), S3_BUCKET, s3_key)

    # Send success notification
    sns_client = boto3.client("sns")
    sns_client.publish(
        TopicArn=SNS_ARN,
        Subject=EMAIL_SUBJECT,
        Message="Tableau UAT Server backup completed successfully."
    )
else:
    # Send failure notification
    sns_client = boto3.client("sns")
    sns_client.publish(
        TopicArn=SNS_ARN,
        Subject=EMAIL_SUBJECT,
        Message=f"Tableau UAT Server backup failed. Backup file {backup_file} not found in {BACKUP_DIR}"
    )
