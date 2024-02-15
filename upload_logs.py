import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime, timedelta
import shutil
import zipfile

def create_zip_folder(local_path, files):
    """
    Creates a zip file for the specified directory.
    """
    zip_file_name = local_path + ".zip"
    with zipfile.ZipFile(zip_file_name, 'w', allowZip64=True) as zipf:
        for file in files:
            zipf.write(os.path.join(local_path, file), file)
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

def collect_logs_older_than_seven_days(logs_dir):
    """
    Collects log files older than seven days from the specified directory.
    """
    logs = []
    seven_days_ago = datetime.now() - timedelta(days=7)
    for file_name in os.listdir(logs_dir):
        file_path = os.path.join(logs_dir, file_name)
        # Check if the current item is a file and not a directory
        if os.path.isfile(file_path):
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if modified_time < seven_days_ago:
                logs.append(file_name)
    return logs

# Specify your local logs folder path
local_logs_root = "/var/opt/tableau/tableau_server/data/tabsvc/logs/"

# Specify your S3 bucket name
s3_bucket_name = "gbt-tableaubucket"

# Specify the base S3 path where logs should be uploaded
s3_upload_base_path = "logs"

# Iterate over subdirectories within the logs group folder
for log_group_folder in os.listdir(local_logs_root):
    local_logs_path = os.path.join(local_logs_root, log_group_folder)
    
    # Collect log files older than seven days
    old_logs = collect_logs_older_than_seven_days(local_logs_path)

    # Create a zip file for old logs
    if old_logs:
        zip_file_path = create_zip_folder(local_logs_path, old_logs)

        # Upload the zip file to S3
        if upload_to_s3(zip_file_path, s3_bucket_name, s3_upload_base_path, local_logs_path):
            # Remove old logs
            for log_file in old_logs:
                os.remove(os.path.join(local_logs_path, log_file))
            print("Old logs from {} moved to S3 successfully.".format(local_logs_path))
        else:
            print("Failed to move old logs from {} to S3.".format(local_logs_path))
    else:
        print("No old logs found in {}.".format(local_logs_path))
