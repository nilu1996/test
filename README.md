Certainly! Below is a Confluence page draft with the given technical instructions for upgrading the Mail Scheduler from version 3.0.2 to the latest version 3.1.0.

---

# Upgrading Mail Scheduler from 3.0.2 to 3.1.0

## Introduction

This document provides step-by-step instructions for upgrading the Mail Scheduler from version 3.0.2 to the latest version 3.1.0.

## Prerequisites

- Ensure you have access to the server where Mail Scheduler is installed.
- Ensure you have the necessary permissions to stop and start services and upload files.
- Backup your current Mail Scheduler configuration.

## Steps for Upgrading

1. **Download the Latest File**
   - Download the latest version of the Mail Scheduler from the [official website](https://docs.infotopics.com/mailscheduler/installation-guide/upgrade).
   - Ensure you download version 3.1.0.

2. **Upload the Latest File to the Tableau Extension Directory**
   - Upload the downloaded file to the specified Tableau extension directory.

3. **Stop the Mail Scheduler Service**
   - Execute the following command to stop the Mail Scheduler service:
     ```bash
     ./mailscheduler-amd64 service stop
     ```

4. **Rename the Old File**
   - Rename the old Mail Scheduler file to keep it as a backup:
     ```bash
     mv mailscheduler-amd64 mailscheduler-amd64-old
     ```

5. **Place the New File in the Same Location**
   - Navigate to the directory where the Mail Scheduler is installed and place the new file there:
     ```bash
     /home/svc_calinuser177/tableau_infotopics
     ```
   - Alternatively, you can copy the file from an S3 bucket:
     ```bash
     aws s3 cp s3://gbt-tableau/mailscheduler-amd64 .
     ```

6. **Make the Mail Scheduler File Executable**
   - Change the file permissions to make the new Mail Scheduler file executable:
     ```bash
     chmod +x mailscheduler-amd64
     ```

7. **Start the Mail Scheduler Service**
   - Start the Mail Scheduler service using the following command:
     ```bash
     ./mailscheduler-amd64 service start
     ```

## Conclusion

By following these steps, you will successfully upgrade the Mail Scheduler to the latest version. If you encounter any issues, refer to the [official documentation](https://docs.infotopics.com/mailscheduler/installation-guide/upgrade) or contact support for assistance.

---

Feel free to copy this draft into your Confluence page and make any additional modifications as needed.
