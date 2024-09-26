Install the RMT Server Using Command Line
Applies to: Tableau Advanced Management
The Resource Monitoring Tool Server (RMT Server) hosts the web application that users interact with. It also does much of the background processing to collate and monitor the data from the Agents. The RMT Server must be installed on dedicated hardware.

This topic describes the steps you can use to install the RMT Server using command line. Command line installation is supported on both Windows and Linux operating systems.

In an effort to align with our company values of Equality, we have changed non-inclusive terminology where possible. Because changing terms in certain places can causing a breaking change, we maintain the existing terminology. So, you may continue to see the terms in CLI commands and options, installation folders, configuration files. and other instances. For more information, see About Tableau Help(Link opens in a new window).

Install on Linux
Install on Windows
To install the RMT Server:

Install the RMT Server:

Download the rpm or .deb RMT Server Installer and save it to a location that you can access from the machine where you plan to install the RMT Server.

Login to the machine where you want the RMT Server installed as a user that has sudo access.

Run the following command to install the RMT Server, where <version> is formatted as major-minor-maintenance:

For RHEL like distribution including CentOS:

sudo yum install <pathtormtserverinstaller>/Tabrmt-Master-x86_64-<version>.rpm

For Ubuntu distributions:

sudo apt install ./<pathtormtserverinstaller>/Tabrmt-Master-amd_64-<version>.deb

This installs the package and the prerequisites including RabbitMQ, Erlang, and a PostgreSQL database. The PostgreSQL database is used to store usage data gathered from Tableau Server. It will then proceed to install the RMT Server.

Initialize RMT Server:

You must explicitly accept the End User License Agreement (EULA) when you initialize RMT Server. You also have the option to specify non-default configurations. To initialize RMT Server with a default configuration, run this command :

sudo /opt/tableau/tabrmt/master/install-scripts/initialize-rmt-master --accepteula
The EULA can be found in the /opt/tableau/tabrmt/master/docs folder.

Beginning in version 2023.1 you can specify a custom Run As account to be used by RMT, as well as other configuration options. By default RMT creates and uses an account called rmt-master to run under. To specify a custom Run As account to be used by RMT Server, include the --unprivileged-user option when you run the initialization script. For information about all the available switches for the initialize-rmt-master script, see RMT Server Initialization Script Options.

Configure the RMT Server
Run the following command as the tabrmt-master user:

sudo su --login tabrmt-master

rmtadmin master-setup [options]

The configuration options can be supplied either through the command prompt, a configuration file. If you do not supply the options, the default values will be applied except for the administrator password. The administrator user name will be set to admin and you will be prompted to provide the password.

Example command including the required password parameter:

rmtadmin master-setup --admin-username=<name of the administrator user> --admin-password=<administrator user password>

The following table lists the required and some commonly used options to configure the RMT Server. For a full list of the configurations options, see rmtadmin Command Line Utility .

Note: Require HTTPS option ensures secure communications between the RMT Server and users. When you require HTTPS for communications, you must also select a mode for the certificate that should be used for these communications. The table below includes the various options. To learn more about these modes and certificates, see SSL Certificate Mode and Requirements

Option	Required?	
Default

Description
admin-password	
Yes

Password can be supplied in the command line or provide a file with the password to use. If neither is provided, you will be prompted for the password.

n/a	The password for the administrator user.
admin-password-file	
No

Password can be supplied in the command line or provide a file with the password to use. If neither is provided, you will be prompted for the password.

n/a	
The file where the password for the administrator user is stored.

Note: tabrmt-master user must have access to this file.

admin-username	No	admin	The username for the administrator user.
http-port	No	80	 
require-https	No	False	Redirect http traffic to HTTPS.
https-certificate-mode	No	
"Default"

Available options:

Default

Local

The type of certificate search to perform for the HTTPS certificate.

Default: This mode uses the default self-signed certificate supplied by the installer.

Local: Allows you to specify a file-based certificate in the /var/opt/tableau/tabrmt/master/config folder.

https-certificate-local-name	
No

Note: If not specified, the Resource Monitoring Tool is installed with a self-signed certificate and will use that certificate for HTTPS communications.

Null	The name of the HTTPS certificate file without the file extension.
https-certificate-local-password	No	Null	The password to use for the HTTPS certificate.
https-certificate-local-password-file	No	Null	The path to the file containing the password to use for the HTTPS certificate.
Create an environment

Run the following command to create an environment:

rmtadmin create-env --name=<myenvironment> --api-username=<TableauServer API user name> --api-password=<password for the Tableau Server API user account>

Configure the environment using the options available for this command. Here are some key configuration options to consider:

The Tableau Server REST API and the Tableau Server Repository configurations are used to communicate with Tableau Server. The Tableau Server Repository configuration is optional, but is a preferred method to access Tableau Server.
You have the option to configure secure encrypted connection when RMT connects to Tableau Server Repository. In order to use SSL connections between RMT and Tableau Server Repository database, Tableau Server must be configured to use SSL. For more information, see Configure SSL for Internal Postgres Communication.

The following table lists the some of the common options. To see a full list of options, see rmtadmin Command Line Utility .

Option	Required?	Default	Description
--name	Yes	n/a	The name of the environment.
--gateway-url	
Yes

 

n/a	
URL used to access the Tableau Server gateway.

--version	Yes	n/a	Tableau Server version that this environment will be monitoring.
--api-username	No	Null	User name of the account used to connect to Tableau Server APIs. The user account should be a Tableau Server administrator with access to all Tableau Server sites.
--api-password	
No

(If you specify the Tableau API user name, you will either provide the password, or specify the file path and file that has the password)

Null

Password of the Tableau Server API user account used to connect to Tableau Server APIs.

--api-password-file	No	Null	The path to the file and the name of the file containing the password of the Tableau Server API user account.
--repository-server	Yes	
Null

This is the server name for the PostgreSQL database that in installed with Tableau Server
--repository-port	Yes	Null	The port number of the Tableau Server Repository database.
--repository-username	Yes	Null	
Username used to connect to PostgreSQL database installed with the Tableau Server Repository.

Resource Monitoring Tool accesses the Tableau Server Repository database directly for performance reasons. For this to work, access to the repository must be enabled, with a password set for the readonly database user. For details, see Enable access to the Tableau Server repository.

--repository-password	Yes	Null	
Password for the user account used to connect to the PostgreSQL database that is installed with the Tableau Server .

Resource Monitoring Tool accesses the Tableau Server Repository database directly for performance reasons. For this to work, access to the repository must be enabled, with a password set for the readonly database user. For details, see Enable access to the Tableau Server repository.

--repository-password-file	No	Null	The path including the file name where the password for the user account used to connect to the PostgreSQL database that is installed with Tableau Server.
--repository-ssl-mode	
No

Prefer	
Tableau Server Repository SSL Mode:

Prefer SSL or Require SSL to configure SSL connections to Tableau Repository.

Disable to never use SSL to make Tableau Server Repository connections.

--repository-ssl-thumbprint	
No

Null	You can choose to either supply the thumbprint that was generated by Tableau Server, or copy the server.crt file to the Resource Monitoring Tool Server(RMT Server) machine. If you choose to copy the certificate file, you don't have to supply the thumbprint. For more information, see Configure Postgres SSL to Allow Direct Connections from Clients.
Download the bootstrap file to a location that can be accessed from the Tableau Server nodes.

rmtadmin bootstrap-file --env=<myenvironment> --filename<The absolute or relative path including the file name>

Optional step - only if not using SSD: The Resource Monitoring Tool is optimized for SSD by default. If you are not using SSD hardware, run the command:

sudo /opt/tableau/tabrmt/master/tabrmt-master optimize --no-ssd

 

Who can do this
To install Resource Monitoring Tool, you must have all the following:

Windows

Administrator permissions on the machine you are installing Resource Monitoring Tool.
Tableau Server Administrator site role.
Resource Monitoring Tool Administrator account.
Linux

Full sudo access for the user account that is used to install the Agent.
Resource Monitoring Tool Administrator account
