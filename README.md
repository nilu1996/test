

Hello Neels,

I had a discussion with our Network and Firewall team regarding the issue with the HRG server.

Although the HRG server can resolve the DNS entry, it encounters issues when publishing data. We have verified from the GBT firewall side, and the team does not observe any traffic originating from the HRG Alteryx server IP address.

Could you please investigate with the HRG Firewall or Network team to determine why the HRG network is blocking traffic to the GBT Tableau URL?

Regarding the IP address, our Tableau Server setup includes a load balancer behind the application. Performing an nslookup on the URLs shows that the IP addresses change every 12 hours, making it impractical to whitelist a specific IP address.

Additionally, the Tableau EC2 instance is assigned a Private IP address. Please take this into account when investigating the issue.

Thank you,
[Your Name]
