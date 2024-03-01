**Maintenance Activity: Update Microsoft Driver Installation on Tableau Server**

---

**Issue Description:**
The Tableau Server encountered a failure on Feb 28, 2024, at 4:06 PM due to the absence of the required Microsoft drivers for SQL Server connectivity. The error message indicates that the necessary drivers are not properly installed on the Tableau Server.

**Error Message:**
```
This job failed on Feb 28, 2024, 4:06 PM after running for 0.0 min because of: com.tableausoftware.server.status.reporting.TableauRuntimeException: The drivers necessary to connect to the database server '10.201.30.110' are not properly installed on Tableau Server. Visit http://www.tableau.com/drivers to download driver setup files. The drivers necessary to connect to the database server '10.201.30.110' are not properly installed on Tableau Server. Visit http://www.tableau.com/drivers to download driver setup files. The drivers required to connect to the data source are not installed. Learn more
```

**Solution:**
To resolve this issue, follow the steps outlined below:

1. **Search for Microsoft SQL Driver:**
   - Navigate to the [Microsoft ODBC Driver for SQL Server installation guide](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15&tabs=alpine18-install%2Credhat17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline#17) to locate the appropriate driver for your Tableau Server.

2. **Check Red Hat Version:**
   - Use the following command to check the Red Hat version of your Tableau Server:
     ```
     cat /etc/redhat-release
     ```
   - Note the Red Hat version for driver compatibility.

3. **Choose Driver and Perform Installation:**
   - Based on the Red Hat version, choose the appropriate driver package from the Microsoft repository.
   - Run the commands below to install the Microsoft ODBC driver:
     ```bash
     # Download appropriate package for the OS version
     # Choose only ONE of the following, corresponding to your OS version
     # RHEL 7 and Oracle Linux 7
     curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo

     # RHEL 8 and Oracle Linux 8
     curl https://packages.microsoft.com/config/rhel/8/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo

     # RHEL 9
     curl https://packages.microsoft.com/config/rhel/9/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo

     sudo yum remove unixODBC-utf16 unixODBC-utf16-devel # to avoid conflicts
     sudo ACCEPT_EULA=Y yum install -y msodbcsql17
     # Optional: for bcp and sqlcmd
     sudo ACCEPT_EULA=Y yum install -y mssql-tools
     echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
     source ~/.bashrc
     # Optional: for unixODBC development headers
     sudo yum install -y unixODBC-devel
     ```

4. **Stop Tableau Server Application:**
   - Execute the following command to stop the Tableau Server application:
     ```
     tsm stop
     ```

5. **Start Tableau Server Application:**
   - Once the Microsoft driver installation is complete, start the Tableau Server application:
     ```
     tsm start
     ```

---

Please execute the above steps to ensure the proper installation of the Microsoft SQL driver on the Tableau Server, resolving the encountered error. Should you require further assistance, feel free to reach out.
