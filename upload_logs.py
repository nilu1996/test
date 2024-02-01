import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime

def upload_to_s3(local_path, bucket_name, s3_base_path):
    """
    Upload a directory to an S3 bucket with a timestamped folder using instance profile credentials.
    """
    s3 = boto3.client('s3')

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

                print("Uploading {} to {}/{}".format(local_file_path, bucket_name, s3_file_path))
                s3.upload_file(local_file_path, bucket_name, s3_file_path)

        print("Upload from {} to {} successful.".format(local_path, s3_path))
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
    print("Logs from {} moved to S3 successfully.".format(local_logs_path_1))
else:
    print("Failed to move logs from {} to S3.".format(local_logs_path_1))

# Upload logs from the second local path
if upload_to_s3(local_logs_path_2, s3_bucket_name, os.path.join(s3_upload_base_path, 'var_backups')):
    print("Logs from {} moved to S3 successfully.".format(local_logs_path_2))
else:
    print("Failed to move logs from {} to S3.".format(local_logs_path_2))
