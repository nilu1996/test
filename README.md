Re-Configure Tableau Server Repository
Applies to: Tableau Advanced Management
Your Tableau Server may be configured to use either a local or an external repository. This topic describes the steps needed to reconfigure your existing Tableau Server with one of the following options:

Move a local Tableau Server Repository to an external repository and configure your Tableau Server to use an external repository.

Move the external Tableau Server Repository to your local Tableau Server installation, and configure your Tableau Server to use the local repository. This means that the Tableau Server repository will be installed on the same machine or machines as your Tableau Server.

To learn more about these options and external repositories, see Tableau Server External Repository.

Move local repository to external
Tableau Server must be stopped to migrate from a local repository to an external repository.

Use the following steps to move Tableau Server Repository from local to external:

Activate the Advanced Management product key on your Tableau Server if it is not already activated. Advanced Management license is required to configure your Tableau Server with an external repository.
Configure Amazon PostgreSQL DB instance to use as the external repository.
Amazon: Create a PostgreSQL DB Instance on AWS Relational Database Service (RDS).
Azure Database: Create a Azure Database PostgreSQL Instance on Azure.
Google Cloud Database: Create a PostgreSQL Instance on Google Cloud
Stand-alone PostgreSQL Instance: Create a PostgreSQL Database as a Stand-alone Installation .
Create a json file with the following configuration settings:

{
 "flavor":"<flavor name>",
 "masterUsername":"<admin user name>",
 "masterPassword":"<password>", 
 "host":"<instance host name>",
 "port":5432
}
flavor: This is the type of external service you are going to use for Tableau Server repository.

Amazon RDS: use “rds”
Azure Database: use "azure"
Google Cloud Database: use "gcp"
Stand-alone PostgreSQL database: use "generic"
masterUsername:

Amazon RDS: Use "rails" for the user name. This is the user that you specified when creating the RDS instance.

You must use "rails" as the masterUsername. This is required for the external repository to work with Tableau Server properly.

Azure Database, Google Cloud instance, and Stand-alone PostgreSQL instance: Choose a user name that meets your requirements. We recommend using postgres as the Administrator user name. If you choose to use a different user name, make sure that the user name does not start with pg, or azure. The user name also cannot be rails, tblwgadmin, tableau, readonly, or tbladminviews.
masterPassword: This is the same password you specified when creating the PostgreSQL database instance.

host: This is the endpoint of your PostgreSQL database instance.

port: The database port you specified when creating the PostgreSQL DB instance.

Run the following TSM CLI command to configure Tableau Server to use external repository:

tsm topology external-services repository enable -f file.json -c <ssl certificate file>.pem

Note: The SSL certificate is needed only if you are using encrypted connections between Tableau Server and the External Repository. If this is not a requirement for you, you must specify the --no-ssl option. In this case, the tsm command would look like this:
tsm topology external-services repository enable -f <filename>.json --no-ssl

The json file is the file that you created in the first step with the configuration settings. The SSL certificate file can be downloaded as described in this topic(Link opens in a new window).

Running the above command will migrate the local repository to your new external PostgreSQL DB instance.

Move external repository to local
Use the following steps to move Tableau Server Repository from external location to the local installation:

Run the following TSM CLI command to move the repository to a specific node:

tsm topology external-services repository disable -n nodeN

If you are setting up HA for your repository, install the repository on a second node. For more information, see Example: Install and Configure a Three-Node HA Cluster.

Note: To install the repository on a second node, you must run the command described in the previous step first. The first step migrates your external repository to the local repository. You can then install the repository on a second node on your Tableau Server.

Who can do this
Tableau Server Administrators can reconfigure external repository. You will also need to have access to create PostgreSQL database instance on Amazon or Azure.



It is worth pointing out here that these changes require the server to be off, and so you will incur some downtime when processing these changes. 
 
A high level idea of the steps you will need to do are as follows: 
1.	Stop the Tableau server with the tsm stop command 
2.	Take a snapshot of the current external repository  
3.	Deploy and restore the snapshot to the encrypted RDS 
4.	Run the tsm commands to move the repository to be local - information here.  
5.	Run the tsm commands to set up the new encrypted RDS as the new repository - information here.  
6.	Start the Tableau server with the tsm start command. 
