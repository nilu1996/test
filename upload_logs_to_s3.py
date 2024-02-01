import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime

def upload_to_s3(local_path, bucket_name, s3_base_path):
    """
    Upload a directory to an S3 bucket with a timestamped folder.
    """
    s3 = boto3.client('s3', aws_access_key_id='ACCESS_KEY', aws_secret_access_key='SECREAT_KEY')

    try:
        # Create timestamped folder
        timestamped_folder = datetime.now().strftime("%Y%m%d_%H%M%S")
        s3_path = os.path.join(s3_base_path, timestamped_folder)

        # Upload files to S3
        for root, dirs, files in os.walk(local_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_path)

                # Create the folder in S3 if it doesn't exist
                s3.put_object(Bucket=bucket_name, Key=os.path.join(s3_path, relative_path) + '/')

                # Add timestamp to the S3 file path
                s3_file_path = os.path.join(s3_path, relative_path)

                print(f"Uploading {local_file_path} to {bucket_name}/{s3_file_path}")
                s3.upload_file(local_file_path, bucket_name, s3_file_path)

        print(f"Upload from {local_path} to {s3_path} successful.")
        return True
    except NoCredentialsError:
        print("Credentials not available.")
        return False

# Specify your local logs folder paths
local_logs_path_1 = "/var/opt"
local_logs_path_2 = "/var/backups"

# Specify your S3 bucket name
s3_bucket_name = "mypythonebucket"

# Specify the base S3 path where logs should be uploaded
s3_upload_base_path = "logs"

# Upload logs from the first local path
if upload_to_s3(local_logs_path_1, s3_bucket_name, os.path.join(s3_upload_base_path, 'var_opt')):
    print(f"Logs from {local_logs_path_1} moved to S3 successfully.")
else:
    print(f"Failed to move logs from {local_logs_path_1} to S3.")

# Upload logs from the second local path
if upload_to_s3(local_logs_path_2, s3_bucket_name, os.path.join(s3_upload_base_path, 'var_backups')):
    print(f"Logs from {local_logs_path_2} moved to S3 successfully.")
else:
    print(f"Failed to move logs from {local_logs_path_2} to S3.")
