Here's a structured Confluence page based on the details you've provided. I've included placeholder links and paths which you can replace with the actual values.

---

# Installing Redshift ODBC and JDBC Drivers on Red Hat-based OS for Tableau Server

## 1. Install Redshift ODBC Drivers

### Step 1: Access Amazon Redshift ODBC Download Documentation
Visit the official Amazon Redshift ODBC download documentation at the following link:
[Amazon Redshift ODBC Download Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html)

### Step 2: Download the RPM Package
As we are working with a Red Hat-based operating system, download the RPM package from the following URL:
[Download RPM Package](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.4.34.1000/AmazonRedshiftODBC-64-bit-1.4.34.1000-1.x86_64.rpm)

### Step 3: Move the Drivers to the Tableau Path
Once downloaded, move the drivers to the Tableau drivers path:
```plaintext
/opt/tableau/tableau_driver/
```

### Step 4: Install the ODBC Driver
Run the following command to install the ODBC driver:
```bash
sudo rpm -ivh /opt/tableau/tableau_driver/AmazonRedshiftODBC-64-bit-1.4.34.1000-1.x86_64.rpm
```

### Step 5: Restart Tableau Server
Restart the Tableau Server to apply the changes:
```bash
tsm restart
```

## 2. Install Redshift JDBC Drivers

### Step 1: Download the JDBC Drivers
Download the JDBC drivers from the following link:
[Download JDBC Drivers](https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/2.0.0.4/AmazonRedshiftJDBC42-2.0.0.4.jar)

### Step 2: Move the Drivers to the Tableau Path
Once downloaded, move the JDBC drivers to the following path:
```plaintext
/opt/tableau/tableau_driver/
```

### Step 3: Restart Tableau Server
Restart the Tableau Server to apply the changes:
```bash
tsm restart
```

---

Feel free to replace the placeholder links and paths with the actual values, and make any adjustments as necessary. This structure provides a clear step-by-step guide for installing both ODBC and JDBC drivers for Amazon Redshift on a Red Hat-based OS for Tableau Server.



https://help.alteryx.com/current/en/license-and-activate/install/download-and-install-a-patch-update.html#download-and-install-a-patch-update


Storage Environments in Alteryx Analytics Cloud
Default Storage Environment:

When you sign up for Alteryx Analytics Cloud, you get a default storage environment.
This default environment stores your data and metadata.
It supports various types of data assets like imported datasets, job results, samples, and temporary files.
Storage Options:

TFS (Trifacta File System):
Managed by Alteryx, no extra setup needed.
Uses AWS S3 buckets managed by Alteryx.
Default storage environment when you first launch the product.
Can be used alongside S3.
S3 (Amazon S3):
Uses your own S3 buckets.
Requires configuration and credentials.
Can be set as the default storage environment or used with TFS.
Choosing and Configuring Storage:

Default Storage Setup:
Initially, TFS is the default storage.
S3 is enabled as secondary storage, requiring setup and credentials.
Changing Default Storage:
You can switch the default storage between TFS and S3.
Ensure you have necessary S3 credentials before switching.
Configure this through the Workspace Settings Page.
S3 Configuration:

Access Modes:
Workspace Mode: All users share the same credentials.
User Mode: Each user has individual credentials (may not be available in all editions).
Authentication Methods:
IAM Role: Recommended, involves creating a role with specific permissions.
Access Keys: Use key-secret combinations for access.
Disabling Access:

Disable S3:
Can be done if TFS is the default storage.
Go to Workspace Settings and disable S3 connectivity.
Disable TFS:
Can be done if S3 is the default storage.
Go to Workspace Settings and disable TFS.
Final Steps:

Verify credentials and configurations.
Apply changes in Workspace Settings.
Ensure assets are stored in the selected default environment.
