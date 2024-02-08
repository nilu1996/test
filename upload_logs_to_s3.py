import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime
import shutil

def create_zip_folder(local_path):
    """
    Creates a zip file for the specified directory.
    """
    zip_file_name = local_path + ".zip"
    shutil.make_archive(local_path, 'zip', local_path)
    return zip_file_name

def upload_to_s3(zip_file_path, bucket_name, s3_base_path, local_path):
    """
    Uploads a zip file to an S3 bucket with a timestamped folder using instance profile credentials.
    """
    s3 = boto3.client('s3')

    try:
        # Create timestamped folder
        timestamped_folder = datetime.now().strftime("%Y%m%d_%H%M%S")
        s3_path = os.path.join(s3_base_path, local_path.replace(os.path.sep, '_'), timestamped_folder)

        # Upload the zip file to S3
        s3_file_path = os.path.join(s3_path, os.path.basename(zip_file_path))
        s3.upload_file(zip_file_path, bucket_name, s3_file_path)

        print("Uploaded {} to {}/{}".format(zip_file_path, bucket_name, s3_file_path))

        print("Upload from {} to {} successful.".format(zip_file_path, s3_path))
        return True
    except NoCredentialsError:
        print("Credentials not available.")
        return False

# Specify your local logs folder paths
local_logs_paths = [
    "/var/opt/tableau/tableau_server/logs",
    "/var/opt/tableau/tableau_server/data/tabsvc/logs/httpd"
]

# Specify your S3 bucket name
s3_bucket_name = "gbt-tableaubucket"

# Specify the base S3 path where logs should be uploaded
s3_upload_base_path = "logs"

# Upload logs from each local path
for local_logs_path in local_logs_paths:
    # Create a zip file for logs from the current local path
    zip_file_path = create_zip_folder(local_logs_path)

    # Upload the zip file to S3
    if upload_to_s3(zip_file_path, s3_bucket_name, s3_upload_base_path, local_logs_path):
        print("Logs from {} moved to S3 successfully.".format(local_logs_path))
    else:
        print("Failed to move logs from {} to S3.".format(local_logs_path))
