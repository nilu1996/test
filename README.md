Certainly! Here's a summary of the provided details along with a technical Confluence documentation:

---

# Script for Log Rotation and Upload to S3

## Overview

The **upload_s3_logs.py** script is designed to manage log rotation in the Tableau Server environment. It collects logs older than 7 days, compresses them into ZIP archives, and uploads the archives to the designated Amazon S3 buckets. This process helps reduce data storage size on the server and ensures efficient log management.

## Script Details

### Script Name:
upload_s3_logs.py

### Python Version:
2.7

### Script Location:
[Specify Script Path]

### Server:
UAT / DEV

### GitHub Location:
[Provide GitHub Repository Link Here]

### Functionality:

- **Log Rotation:** The script scans the log folder on the Tableau Server and identifies logs that are older than 7 days.
- **Compression:** It compresses the identified logs into ZIP archives to save space and facilitate efficient storage and transfer.
- **Upload to S3:** The script uploads the compressed log archives to the specified Amazon S3 buckets, segregating logs based on the environment (DEV or UAT).

### Bucket Names:

- **For DEV:** [Specify DEV Bucket Name]
- **For UAT:** [Specify UAT Bucket Name]

## Implementation Steps

To deploy and configure the **upload_s3_logs.py** script, follow these steps:

1. **Download the Script:**
   - Download the **upload_s3_logs.py** script from the specified GitHub location or copy it to the designated location on the server.

2. **Set Up Python Environment:**
   - Ensure Python 2.7 is installed on the server where the script will be executed.

3. **Configure Script Parameters:**
   - Open the script in a text editor.
   - Verify and update any configurable parameters such as S3 bucket names, log folder paths, or retention periods as per your requirements.

4. **Install Dependencies:**
   - If the script relies on external libraries or modules, ensure they are installed in the Python environment.

5. **Test Execution:**
   - Run the script manually to verify its functionality.
   - Confirm that logs older than 7 days are correctly identified, compressed, and uploaded to the respective S3 buckets.

6. **Schedule Execution (Optional):**
   - Set up a cron job or task scheduler to automate the execution of the script at regular intervals for periodic log rotation and upload.

## Conclusion

The **upload_s3_logs.py** script provides an automated solution for log rotation and management in the Tableau Server environment. By compressing and uploading older logs to Amazon S3, organizations can optimize storage space usage and maintain efficient log retention practices.

---

Feel free to customize the content further to include any additional details or specifications relevant to your deployment environment or requirements!
