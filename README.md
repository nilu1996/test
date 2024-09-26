Install the Agent Using Command Line
Applies to: Tableau Advanced Management
The Agent is a lightweight process that consumes minimal server resources and sends data to the Resource Monitoring Tool Server (RMT Server). Install the Resource Monitoring Tool Agent on each of your Tableau Server nodes. To install and register an Agent, download the Agent bootstrap configuration file and save it to a location that is accessible from the Resource Monitoring Tool Agent nodes.

This topic describes the steps you can use to install the Resource Monitoring Tool Agent using command line. Command line installation is supported on both Windows and Linux operating systems.

In an effort to align with our company values of Equality, we have changed non-inclusive terminology where possible. Because changing terms in certain places can causing a breaking change, we maintain the existing terminology. So, you may continue to see the terms in CLI commands and options, installation folders, configuration files. and other instances. For more information, see About Tableau Help(Link opens in a new window).

Before you install
Download the bootstrap file and save it to a location that is accessible to the nodes on which you are going to install RMT Agent. Bootstrap files are only valid for 24 hours after downloading.  You will need to regenerate the bootstrap file if the one you are using is older than 24 hours.
Starting in version 2021.3, Agent registration will need to communicate both through a https endpoint and RabbitMQ to complete Agent registration. Make sure both ports 443 and 5672 are open for these communcations.
Install on Linux
Install on Windows
To install and configure the Agent:

Install:
Download the .rpm or .deb Agent Installer and save it to a location that you can access from the machine where you plan to install the Agent.

Run the following command to install the Agent where <version> is formatted as major-minor-maintenance:

For RHEL like distributions including CentOS:

sudo yum install Tabrmt-Agent-x86_64-<version>.rpm

For Ubuntu:

sudo apt install Tabrmt-Agent-amd64-<version>.deb

Initialize RMT Agent:

You must explicitly accept the End User License Agreement (EULA) when you initialize RMT Agent. You also have the option to specify non-default configurations. To initialize RMT Agent with a default configuration, run this command :

sudo /opt/tableau/tabrmt/agent/install-scripts/initialize-rmt-agent --accepteula
The EULA can be found in the /opt/tableau/tabrmt/agent/docs folder.

Beginning in version 2023.1 you can specify a custom Run As account to be used by RMT, as well as other configuration options. By default RMT creates and uses an account called rmt-agent to run under. To specify a custom Run As account to be used by RMT Agent, include the --unprivileged-user option when you run the initialization script. For information about all the available switches for the initialize-rmt-agent script, see RMT Agent Initialization Script Options.

Register:
Log off and log on as the tabrmt-agent user so you can run rmtadmin commands which always require that you run as the tabrmt-agent user. Also,when you log on again, you create a new session in which group membership changes have taken effect.

sudo su --login tabrmt-agent

Run the following command and provide the path where the bootstrap file is located. Provide a description of the node where the Agent is being installed.

rmtadmin register <bootstrap file path\file> --server-name=<Friendly name of machine> --server-description=<server description> --username=<name of the RMT admin user>

You will be prompted for the password of the RMT admin user.

Note: The tabrmt-agent user defaults to run commands from the base working directory: /var/opt/tableau/tabrmt/agent, so you must specify the file path accordingly. For example, if you placed the bootstrap file in the /var/opt/tableau/tabrmt/agent/bootstrap/ folder as recommended, the file path would be /var/opt/tableau/tabrmt/agent/bootstrap/<bootstrap_file_name>.

The following table lists the configuration options used to register the Agent:

Option	Required?	Default	Description
--bootstrap file	Yes	<none>	The location of the bootstrap file.
--username	Yes	<none>	This is typically the admin user you created during RMT Server installation.
--password	Yes	<none>	This is the password for the user account
--password-file	
No

Password can be supplied in the command line or a file that contains the password. If neither is provided, you will be prompted for the password.

<none>	Path including the file name where the password is stored.
-- server-name	No	Host name of machine	Name of the computer that has the Agent Installed. If no option is provided, this field will default to the host name of the machine.
--server-description	No	<none>	Description of the computer that has the Agent installed. If no option is provided, this field will remain blank.
Installing Agent on Multi-Node Tableau Server
Run the steps described above on each of the nodes of Tableau Server. On the web interface of the RMT Server you should be able to see all the nodes where the Agent is installed.

