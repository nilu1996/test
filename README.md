Create a Custom systemd Service
Create Unit File: Create a unit file named myservice.service in the directory /lib/systemd/system/ with the following content:
     
 [Unit]
Description=Extension Name Service
After=network.target
[Service]
User=root
WorkingDirectory=/usr/local/bin
ExecStart=/usr/local/bin/super-tables-linux --port 443 --cert yourdomain.crt --key yourdomain.key
Restart=on-abort
[Install]
WantedBy=multi-user.target


Copy and Set Permissions
2.	Copy Unit File: Copy the unit file to /etc/systemd/system/:
sudo cp /lib/systemd/system/myservice.service /etc/systemd/system/myservice.service 
3.	Set Permissions: Set appropriate permissions for the unit file:
sudo chmod 644 /etc/systemd/system/myservice.service 
Start and Enable the Service
4.	Start the Service: Start the service using systemctl:
sudo systemctl start myservice 
5.	Check Service Status: Check the status of the service to ensure it's running:
sudo systemctl status myservice 
If everything is set up correctly, you should see output indicating that the service is active and running.
Stop or Restart the Service
6.	Stop or Restart Service: You can stop or restart the service using systemctl:
sudo systemctl stop myservice sudo systemctl restart myservice 
Enable Service at Boot
7.	Enable Service: To ensure the service starts automatically on boot, enable it:
sudo systemctl enable myservice 
This creates a symlink to the unit file in the appropriate target.
Reboot and Verify
8.	Reboot: Reboot your system, either through the Linode Manager or using the appropriate command for your system.
9.	Check Service Status After Reboot: After rebooting, verify that the service started correctly:
sudo systemctl status myservice 
You should see output indicating that the service is active and running after the system boots up.

