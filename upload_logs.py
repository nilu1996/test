import os
import datetime
import boto3
from botocore.exceptions import NoCredentialsError

# Set the default region for boto3 globally
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

# Define paths
BACKUP_DIR = "/var/opt/tableau/tableau_server/data/tabsvc/files/backups/"
S3_BUCKET = "gbt-uattableau"
S3_PREFIX = "backup/"
SNS_ARN = "arn:aws:sns:us-east-1:090124397890:Instance-Health-monitoring"
EMAIL_SUBJECT = "Tableau Server Backup Notification"

# Run Tableau backup command
backup_file = "backup.tsbak"
backup_command = "tsm maintenance backup -f {} -d".format(backup_file)
os.system(backup_command)

# Check if backup file exists
if os.path.isfile(os.path.join(BACKUP_DIR, backup_file)):
    # Move backup file to specific location
    backup_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_backup_file = "backup_{}.tsbak".format(backup_time)
    os.rename(os.path.join(BACKUP_DIR, backup_file), os.path.join(BACKUP_DIR, new_backup_file))
    
    # Remove older backup files
    for file in os.listdir(BACKUP_DIR):
        if file.startswith("backup_") and file.endswith(".tsbak"):
            file_time = datetime.datetime.strptime(file[7:-6], "%Y%m%d%H%M%S")
            if (datetime.datetime.now() - file_time) > datetime.timedelta(days=7):
                os.remove(os.path.join(BACKUP_DIR, file))

    try:
        # Move backup file to S3 bucket
        s3_client = boto3.client("s3")  # No need to specify region here
        s3_key = S3_PREFIX + new_backup_file
        s3_client.upload_file(os.path.join(BACKUP_DIR, new_backup_file), S3_BUCKET, s3_key)

        # Send success notification
        sns_client = boto3.client("sns")  # No need to specify region here
        sns_client.publish(
            TopicArn=SNS_ARN,
            Subject=EMAIL_SUBJECT,
            Message="Tableau UAT Server backup completed successfully."
        )
    except NoCredentialsError:
        # Send failure notification (no AWS credentials)
        sns_client = boto3.client("sns")  # No need to specify region here
        sns_client.publish(
            TopicArn=SNS_ARN,
            Subject=EMAIL_SUBJECT,
            Message="Tableau UAT Server backup failed. No AWS credentials found."
        )
else:
    # Send failure notification (backup file not found)
    sns_client = boto3.client("sns")  # No need to specify region here
    sns_client.publish(
        TopicArn=SNS_ARN,
        Subject=EMAIL_SUBJECT,
        Message="Tableau UAT Server backup failed. Backup file {} not found in {}".format(backup_file, BACKUP_DIR)
    )
