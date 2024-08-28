RMT Master Setup :

1. Download the rpm or .deb RMT Server Installer and save it to a location that you can access from the machine where you plan to install the RMT Server.

sudo yum install Tabrmt-Agent-x86_64-<version>.rpm

2. Login to the machine where you want the RMT Server installed as a user that has sudo access.

3. Run the following command to install the RMT Server, where <version> is formatted as major-minor-maintenance:

   sudo yum install <pathtormtserverinstaller>/Tabrmt-Master-x86_64-<version>.rpm
   
   This installs the package and the prerequisites including RabbitMQ, Erlang, and a PostgreSQL database. The PostgreSQL database is used to store usage data gathered from Tableau Server. It will then proceed to install the RMT Server
   
4. Initialize RMT Server:

   You must explicitly accept the End User License Agreement (EULA) when you initialize RMT Server. 
   You also have the option to specify non-default configurations. To initialize RMT Server with a default configuration.
   
   sudo /opt/tableau/tabrmt/master/install-scripts/initialize-rmt-master --accepteula
   
5. Configure the RMT Server
   sudo su --login tabrmt-master
   rmtadmin master-setup [options]
   
   If you do not supply the options, the default values will be applied except for the administrator password. The administrator user name will be set to admin and you will be prompted to provide the password.
   
   Example command including the required password parameter:

   rmtadmin master-setup --admin-username=<name of the administrator user> --admin-password=<administrator user password>
   
6. Create an environment
   Run the following command to create an environment:
   rmtadmin create-env --name=<myenvironment> --api-username=<TableauServer API user name> --api-password=<password for the Tableau Server API user account>
   
   --name = production
   --api-username = 
   --api-passoword = 
   
7. Download the bootstrap file to a location that can be accessed from the Tableau Server nodes.

   rmtadmin bootstrap-file --env=<myenvironment> --filename<The absolute or relative path including the file name>
   
8. Optional step - only if not using SSD:

   sudo /opt/tableau/tabrmt/master/tabrmt-master optimize --no-ssd
   
   


RMT Agent Installtion :

Before you install
Download the bootstrap file and save it to a location that is accessible to the nodes on which you are going to install RMT Agent. Bootstrap files are only valid for 24 hours after downloading.  You will need to regenerate the bootstrap file if the one you are using is older than 24 hours.

Starting in version 2021.3, Agent registration will need to communicate both through a https endpoint and RabbitMQ to complete Agent registration. Make sure both ports 443 and 5672 are open for these communcations.

Install:
Download the .rpm or .deb Agent Installer and save it to a location that you can access from the machine where you plan to install the Agent.

1. Run the following command to install the Agent where <version> is formatted as major-minor-maintenance:

   For RHEL like distributions including CentOS:

   sudo yum install Tabrmt-Agent-x86_64-<version>.rpm
   
2. Initialize RMT Agent:
   You must explicitly accept the End User License Agreement (EULA) when you initialize RMT Agent. You also have the option to specify non-default configurations. To initialize RMT Agent with a default configuration, run this command :
   
   sudo /opt/tableau/tabrmt/agent/install-scripts/initialize-rmt-agent --accepteula
   
   The EULA can be found in the /opt/tableau/tabrmt/agent/docs folder.
   
   Beginning in version 2023.1 you can specify a custom Run As account to be used by RMT, as well as other configuration options. By default RMT creates and uses an account called rmt-agent to run under. To specify a custom Run As account to be used by RMT Agent, include the --unprivileged-user option when you run the initialization script. For information about all the available switches for the initialize-rmt-agent
   
3. Register:
   Log off and log on as the tabrmt-agent user so you can run rmtadmin commands which always require that you run as the tabrmt-agent user. Also,when you log on again, you create a new session in which group membership changes have taken effect.

   sudo su --login tabrmt-agent
   
   Run the following command and provide the path where the bootstrap file is located. Provide a description of the node where the Agent is being installed.
   
   rmtadmin register <bootstrap file path\file> --server-name=<Friendly name of machine> --server-description=<server description> --username=<name of the RMT admin user>
   
   You will be prompted for the password of the RMT admin user.
   
   Note: The tabrmt-agent user defaults to run commands from the base working directory: /var/opt/tableau/tabrmt/agent, so you must specify the file path accordingly. For example, if you placed the bootstrap file in the /var/opt/tableau/tabrmt/agent/bootstrap/ folder as recommended, the file path would be /var/opt/tableau/tabrmt/agent/bootstrap/<bootstrap_file_name>.
   
