import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime
import zipfile

def create_zip_file(directory):
    """
    Creates a zip file containing all files in the given directory.
    """
    zip_file_name = directory + '.zip'
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))
    return zip_file_name

def upload_to_s3(local_path, bucket_name, s3_base_path):
    """
    Uploads a directory to an S3 bucket with a timestamped folder using instance profile credentials.
    """
    s3 = boto3.client('s3')

    try:
        # Create timestamped folder
        timestamped_folder = datetime.now().strftime("%Y%m%d_%H%M%S")
        s3_path = os.path.join(s3_base_path, timestamped_folder)

        # Create a zip file containing all files in the directory
        zip_file = create_zip_file(local_path)

        # Upload the zip file to S3
        s3_file_path = os.path.join(s3_path, os.path.basename(zip_file))
        s3.upload_file(zip_file, bucket_name, s3_file_path)

        print("Uploaded {} to {}/{}".format(zip_file, bucket_name, s3_file_path))

        # Remove the temporary zip file
        os.remove(zip_file)

        print("Upload from {} to {} successful.".format(local_path, s3_path))
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
