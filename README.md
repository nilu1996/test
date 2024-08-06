Reconfigure Tableau Server Repository
Overview
This guide outlines the steps to reconfigure the Tableau Server repository, including stopping the server, taking a snapshot, deploying the snapshot, and setting up a new repository.

Steps
Stop Tableau Server

Ensure no active connections by stopping Tableau Server.
Command: tsm stop
Take a Snapshot of the Current Repository

Create a snapshot of your current PostgreSQL repository.
Amazon RDS: Use AWS Management Console or AWS CLI.
Deploy and Restore Snapshot to Encrypted RDS

Restore the snapshot to an encrypted RDS instance.
Amazon RDS: Create a new RDS instance with encryption enabled.
Move Repository to Local (if needed)

If moving from an external to a local repository, disable the external repository.
Command: tsm topology external-services repository disable -n nodeN
Set Up New Encrypted RDS as Repository

Create a JSON configuration file with the following settings:
json
Copy code
{
  "flavor": "<flavor name>",
  "masterUsername": "<admin user name>",
  "masterPassword": "<password>", 
  "host": "<instance host name>",
  "port": 5432
}
Configure Tableau Server to use the new RDS instance.
Command:
bash
Copy code
tsm topology external-services repository enable -f <file.json> -c <ssl certificate file>.pem
If SSL is not required, use:
bash
Copy code
tsm topology external-services repository enable -f <file.json> --no-ssl
Start Tableau Server

Restart Tableau Server to apply changes.
Command: tsm start
