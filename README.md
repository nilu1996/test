

Procedure: Encrypt RDS and Move Tableau Repository to External RDS

1. Stop Tableau Services
Execute the following command to stop all Tableau services:
```bash
tsm stop
```

2. Take Snapshot from External RDS DB
Follow these steps to take a snapshot of your existing unencrypted RDS instance:
1. Navigate to the RDS console.
2. Select the RDS instance you want to snapshot.
3. Choose Actions > Take Snapshot.
4. Provide a name for the snapshot and proceed.

3. Launch a New RDS Instance with Encrypted Storage
To encrypt your existing RDS instance:
1. Follow the instructions in this [AWS guide](https://dev.to/aws-builders/how-to-encrypt-an-unencrypted-rds-db-instance-262g) to restore the snapshot into a new encrypted RDS instance.

4. Disable the Current External Repository in Tableau
To move the Tableau repository to a new node:
```bash
tsm topology external-services repository disable -n node1
```
Note:
- Ensure that `node1` is the correct node where your current external repository is hosted. Replace `node1` with the correct node name if necessary.

5. Move Local Repository to the External RDS
Create a JSON file named `external-repository.json` with the following content:
```json
{
  "flavor": "rds",
  "masterUsername": "Username",
  "masterPassword": "password",
  "host": "tsm-dev-stack-3-rdsinstance-nvsdehq2ewzm.cwicosnm4qi7.us-east-1.rds.amazonaws.com",
  "port": 5432
}
```
Replace `Username` and `password` with your actual RDS credentials.

6. Enable the New External Repository
Run the following command to enable the external repository using the JSON file:
```bash
tsm topology external-services repository enable -f external-repository.json -c <ssl certificate file>.pem
```

Note:
- Replace `<ssl certificate file>` with the path to your SSL certificate file.
- If you are not using an encrypted connection between the Tableau Server and RDS, you might skip the `-c` option.

7. Verify SSL Configuration (Optional)
If you are unsure whether an encrypted connection is used, run:
```bash
tsm configuration get -k pgsql.ssl.enabled
```
If the response is `false`, SSL is not enabled between Tableau Server and the RDS instance.

8. Final Steps
- After ensuring that the repository is properly set up with the external RDS, start the Tableau services:
  ```bash
  tsm start
  ```

---

