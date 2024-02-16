Certainly! Below are separate documents for Tableau Server backup and restore processes for both single node and multiple node deployments:

---

**Tableau Server Backup and Restore Process (Single Node)**

**Backup Process:**

1. Log in to the AWS Console.
2. Select the server where Tableau Server is installed.
3. To perform a backup, execute the following command:

    ```
    tsm maintenance backup -f backup.tsbak -d
    ```

4. Export all settings using the following command:

    ```
    tsm settings export -f <filename>.json
    ```

   The backup file is generated in the temporary location:

   ```
   /var/opt/tableau/tableau_server/data/tabsvc/files/backups/<filename>.tsbak
   ```

**Restore Process:**

1. Ensure the backup file is in the default location:

   Location: `/var/opt/tableau/tableau_server/data/tabsvc/files/backups/<filename>.tsbak`

   Note: Check the backup date before restoring.

2. Execute the following commands to restore the backup:

    ```
    tsm stop  // Stop the server first
    tsm settings import -f <filename>.json  // Import settings first
    tsm pending-changes apply   
    tsm maintenance restore -f backup-2024-02-14.tsbak
    tsm restart 
    ```

---

**Tableau Server Backup and Restore Process (Multiple Nodes - Node 1)**

**Backup Process:**

1. Log in to the AWS Console.
2. Select Node 1 where Tableau Server is installed.
3. Execute the following command to perform a backup:

    ```
    tsm maintenance backup -f backup.tsbak -d
    ```

4. Export all settings using the command:

    ```
    tsm settings export -f <filename>.json
    ```

   The backup file is generated in the temporary location:

   ```
   /var/opt/tableau/tableau_server/data/tabsvc/files/backups/<filename>.tsbak
   ```

**Restore Process:**

1. Ensure the backup file is in the default location:

   Location: `/var/opt/tableau/tableau_server/data/tabsvc/files/backups/<filename>.tsbak`

   Note: Check the backup date before restoring.

2. Execute the following commands to restore the backup:

    ```
    tsm stop  // Stop the server first
    tsm settings import -f <filename>.json  // Import settings first
    tsm pending-changes apply   
    tsm maintenance restore -f backup-2024-02-14.tsbak
    tsm restart 
    ```

---

These documents provide step-by-step instructions for backing up and restoring Tableau Server for both single node and multiple node deployments, with specific details for each scenario.
