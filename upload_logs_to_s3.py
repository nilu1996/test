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

def upload_to_s3(zip_file_path, bucket_name, s3_base_path):
    """
    Uploads a zip file to an S3 bucket with a timestamped folder using instance profile credentials.
    """
    s3 = boto3.client('s3')

    try:
        # Create timestamped folder
        timestamped_folder = datetime.now().strftime("%Y%m%d_%H%M%S")
        s3_path = os.path.join(s3_base_path, timestamped_folder)

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
local_logs_path_1 = "/var/opt/tableau/tableau_server/logs"
local_logs_path_2 = "/var/opt/tableau/tableau_server/data/tabsvc/logs/httpd"

# Specify your S3 bucket name
s3_bucket_name = "gbt-tableaubucket"

# Specify the base S3 path where logs should be uploaded
s3_upload_base_path = "logs"

# Create a zip file for logs from the first local path
zip_file_path_1 = create_zip_folder(local_logs_path_1)

# Upload the zip file to S3
if upload_to_s3(zip_file_path_1, s3_bucket_name, os.path.join(s3_upload_base_path, 'var_opt')):
    print("Logs from {} moved to S3 successfully.".format(local_logs_path_1))
else:
    print("Failed to move logs from {} to S3.".format(local_logs_path_1))

# Create a zip file for logs from the second local path
zip_file_path_2 = create_zip_folder(local_logs_path_2)

# Upload the zip file to S3
if upload_to_s3(zip_file_path_2, s3_bucket_name, os.path.join(s3_upload_base_path, 'var_backups')):
    print("Logs from {} moved to S3 successfully.".format(local_logs_path_2))
else:
    print("Failed to move logs from {} to S3.".format(local_logs_path_2))
