import os
import subprocess
import boto3
import botocore

# Define paths
BACKUP_DIR = "/var/opt/tableau/tableau_server/data/tabsvc/files/backups/"
S3_BUCKET = "s3://gbt-uattableau/backup/"
SNS_ARN = "arn:aws:sns:us-east-1:090124397890:Instance-Health-monitoring"
EMAIL_SUBJECT = "Tableau Server Backup Notification"

# Run Tableau backup command
backup_file = "backup-2024-03-04.tsbak"
subprocess.run(["tsm", "maintenance", "backup", "-f", backup_file, "-d"], cwd=BACKUP_DIR)

# Check if backup files exist
if os.path.exists(os.path.join(BACKUP_DIR, backup_file)):
    # Move backup file to S3 bucket
    s3_key = "{}/{}".format(S3_BUCKET, backup_file)
    s3_client = boto3.client("s3", config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    s3_client.upload_file(os.path.join(BACKUP_DIR, backup_file), s3_key)

    # Remove old backup files (Example: Remove files older than 7 days)
    # Implement your logic here

    # Send success notification
    sns_client = boto3.client("sns", config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    sns_client.publish(
        TopicArn=SNS_ARN,
        Subject=EMAIL_SUBJECT,
        Message="Tableau UAT Server backup completed successfully.",
    )
else:
    # Send failure notification
    sns_client = boto3.client("sns", config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    sns_client.publish(
        TopicArn=SNS_ARN,
        Subject=EMAIL_SUBJECT,
        Message="Tableau UAT Server backup failed. Backup file {} not found in {}".format(backup_file, BACKUP_DIR),
    )
