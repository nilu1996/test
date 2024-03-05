Subject: Technical Discussion on S3 POC Approach

Hi Chandan,

I hope this email finds you well. Today, I had a discussion with the team regarding our S3 Proof of Concept (POC) approach, and I'd like to share the key points with you:

User Restriction:
1. We can implement user restrictions at the bucket level to control access.

Requirements from Our Side:
To proceed with the implementation, we require the following details:
1. ROLE ARN name
2. Destination S3 bucket name
3. AWS Account details

Upload and Download Process:

Uploading Files:
1. Users will receive their username and password from the MFT team to facilitate file uploads.
2. The downloading process will be scheduled. At specific times, the data will be available on the GoAnywhere server.

Please let me know if you need any further clarification or if there are any additional details required from your end.

Best regards,
[Your Name]


Subject: Discussion Outcome: Implementation of Customer Managed KMS Keys for Backup

Hi Chandan,

I hope you're doing well. I wanted to update you on the recent discussion I had with the CloudOps and Backup teams regarding our backup strategy.

The Backup team has highlighted the necessity of utilizing Customer Managed KMS keys to mitigate potential failures in our backup processes. It's imperative that we attach these keys to the volumes of our EC2 instances to ensure data security and compliance.

To achieve this objective, we've explored two potential approaches:

1. Redeploying CloudFormation Templates (CFT) with KMS keys:
   We've considered this approach; however, deploying from scratch might introduce complexities and potential disruptions to our existing infrastructure. Therefore, we've decided to explore alternative methods.

2. Creating KMS keys, Volume Snapshot, and Volume Attachment:
   In this approach, we will:
   - Create the required KMS keys.
   - Take a snapshot of the volumes.
   - Create new volumes from the snapshot and attach the KMS keys.
   - Finally, attach these new snapshot volumes to the respective EC2 instances.

It's important to note that implementing this approach might incur some downtime due to the volume attachment process.

I would appreciate your input on the proposed approach and any suggestions you might have regarding its implementation. Please let me know your thoughts on this matter at your earliest convenience.

Looking forward to your response.

Best regards,
[Your Name]
