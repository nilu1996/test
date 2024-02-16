Subject: Technical Details for Ticket UA-3765 - Proof of Concept (POC)

Hi Chandan,

Please find below the technical outline for the proof of concept (POC):

1. Creation of an IAM role is required to grant access to the S3 bucket designated for file storage.
2. Configuration of Access Key and Secret Key is necessary for integration with the SFTP cloud. Please provide the relevant URL for setup.
3. Upon setup, the SFTP cloud will provide us with the hostname and password for establishing communication between our local system and the SFTP cloud.
4. Workflow:
   - Once the connection is established with the SFTP cloud, files added from our local system will be reflected in the S3 bucket.
5. Setting up SFTP on a Windows server requires installation of OpenSSH on the local machine.
6. User setup is required from the Burp Suite team's end. Once the user has OpenSSH installed, we will provide them with the hostname and password for access.

Note: To proceed with this POC, I require OpenSSH installed for testing purposes, which is the reason behind raising this ticket.

Kindly review the approach outlined above and let me know if any adjustments are needed or if further exploration is required.

Best regards,
[Your Name]
