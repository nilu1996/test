Update on Extension Installation for Tableau Infotopics.

Steps need to followed while doing this Extension Installation 

1. We need to have 1 extension 
     aft-extensions-manager-linux-1.2.0 : Using this installation we can get other extension installed. 

2. When we extract zip file for this extension it give bash script type file which we run using
    sudo ./aft-extensions-manager

3. It will start running the service. It will open port which will be available. 
    Ex: http://10.201.165.244:33363
    In same time we need to open the service in browser and follow the instruction given over web ui
    Is should be like this
    Online configuration and features - Infotopics | Apps for Tableau

4. Blocker:
    We need to have firewall request to allow this particular port which is open by same time when we run this extension manager file. I have observed that this port and accordingly raised the support request: https://amexgbt.freshservice.com/support/tickets/1581454
Once its done, I will connect with Udbhav for to do configuration from browser side if needed.
