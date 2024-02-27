1. /tmp/automated-installer -a tsmadmin -f /tmp/config.json -r /tmp/registration.json -s /tmp/secrets.properties TSRX-8C86-1230-CAB3-DA4F -v --accepteula --force /tmp/tableau-server.rpm
   - This command is likely running an automated installer for Tableau Server.
   - It installs Tableau Server using the provided configuration, registration, and secret files.
   - `tsmadmin` is the username used for administrative tasks.
   - `-v` enables verbose output.
   - `--accepteula` automatically accepts the End User License Agreement.
   - `--force` forces the installation even if a previous version exists.
   - `/tmp/tableau-server.rpm` is the path to the Tableau Server RPM file.
   
2. source /etc/profile.d/tableau_server.sh
   - This command sources a shell script (`tableau_server.sh`) located in the `/etc/profile.d/` directory.
   - It likely sets environment variables or performs other setup tasks related to Tableau Server.

3. tsm status
   - This command checks the status of Tableau Services Manager (TSM), which manages Tableau Server processes.
   
4. tsm stop
   - This command stops all Tableau Server processes.

5. tsm topology nodes get-bootstrap-file --file /tmp/bootstrap.json
   - This command generates a bootstrap configuration file (`bootstrap.json`) containing information about the Tableau Server topology.
   
6. aws s3 cp /tmp/bootstrap.json s3://gbt-tableaubucket/dev-tsm-backups/bootstrap.json
   - This command copies the generated bootstrap file to an Amazon S3 bucket named `gbt-tableaubucket` under the `dev-tsm-backups` directory.
   
7. tsm topology external-services repository enable -f /tmp/rdsconfig.json --no-ssl
   - This command configures Tableau Server to use an external repository service (e.g., RDS) using the settings specified in the `rdsconfig.json` file.
   - `--no-ssl` disables SSL for communication with the external repository.
   
8. cd /tmp/
   - Changes the current directory to `/tmp/`.
   
9. ls
   - Lists the contents of the current directory.
   
10. cat rdsconfig.json
    - Displays the contents of the `rdsconfig.json` file.
    
11. vi rdsconfig.json
    - Opens the `rdsconfig.json` file for editing using the vi text editor.
    
12. tsm status -v
    - Checks the status of Tableau Services Manager (TSM) with verbose output.
    
13. curl localhost
    - Sends an HTTP request to the local machine (`localhost`).
    
14. systemctl status firewalld
    - Checks the status of the firewalld service.
    
15. iptables -l
    - Lists the current IP packet filter rules.
    
16. clear
    - Clears the terminal screen.
    
17. tsm licenses deactivate -k TSRX-8C86-1230-CAB3-DA4F
    - Deactivates a Tableau Server license key specified by `TSRX-8C86-1230-CAB3-DA4F`.
    
18. tsm start
    - Starts all Tableau Server processes.
    
19. tsm licenses list
    - Lists all Tableau Server license keys.
