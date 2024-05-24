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
