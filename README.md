  Tableau Cluster:
  Run command from node 1 (Master)
  tsm maintenance backup -f backup.tsbak -d
  tsm settings export -f <filename>.json : 
  
  The backup file is assembled in a temporary location in the data directory
   
  /var/opt/tableau/tableau_server/data/tabsvc/files/backups/<filename>.tsbak
  
  
   Restore:
   
   Make sure backup file should be in default location where we are taking Backup
   location: /var/opt/tableau/tableau_server/data/tabsvc/files/backups/<filename>.tsbak
   
   Note: Check date when we trying to restore the backup. 
   
   tsm stop  -- stop the server first 
   tsm settings import -f <filename>.json
   tsm pending-changes apply
   tsm maintenance restore -f backup-2024-02-14.tsbak
   tsm restart 
