Please help me with write tablau conflucen documentation. You can add your inputs I need full doucmetation input to create maintance actitity page

Update Microsoft driver not installled on tableua server
Getting below error

This job failed on Feb 28, 2024, 4:06 PM after running for 0.0 min because of: com.tableausoftware.server.status.reporting.TableauRuntimeException: The drivers necessary to connect to the database server '10.201.30.110' are not properly installed on Tableau Server. Visit http://www.tableau.com/drivers to download driver setup files. The drivers necessary to connect to the database server '10.201.30.110' are not properly installed on Tableau Server. Visit http://www.tableau.com/drivers to download driver setup files. The drivers required to connect to the data source are not installed. Learn more

Solution:
1. Serach for Microsoft driver sql driver by following link
https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15&tabs=alpine18-install%2Credhat17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline#17

2. Check Tableau server os version
   Helo me with radhat version check command here

3. Choosed driver accordingly and perform stpes one by one

ex: 
#Download appropriate package for the OS version
#Choose only ONE of the following, corresponding to your OS version

#RHEL 7 and Oracle Linux 7
curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo

#RHEL 8 and Oracle Linux 8
curl https://packages.microsoft.com/config/rhel/8/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo

#RHEL 9
curl https://packages.microsoft.com/config/rhel/9/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo

sudo yum remove unixODBC-utf16 unixODBC-utf16-devel #to avoid conflicts
sudo ACCEPT_EULA=Y yum install -y msodbcsql17
# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y yum install -y mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
# optional: for unixODBC development headers
sudo yum install -y unixODBC-devel

4. Stop Applucation: TSM Stop

5. Start the APplication:
   tsm start
