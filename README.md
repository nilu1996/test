1. Creation of an IAM role is required to grant access to the S3 bucket designated for file storage.
2. Configuration of Access Key and Secret Key is necessary for integration with the SFTP cloud. https://app.sftpcloud.io/
3. Upon setup, the SFTP cloud will provide us with the hostname and password for establishing communication between our local system and the SFTP cloud.
4. Workflow:
   - Once the connection is established with the SFTP cloud, files added from our local system will be reflected in the S3 bucket.
5. Setting up SFTP on a Windows server requires installation of OpenSSH on the local machine.
6. Once the user has OpenSSH installed, we will provide them with the hostname and password for access.
