**KMS Key Rotation Activity Plan**

1. **Activity Date:** [Insert Activity Date]

2. **SNAP Ticket Request:**
   - Raise SNAP ticket for KMS key rotation activity.

3. **Check Application Impact from Vendor Team:**
   - Coordinate with the Vendor team to assess the impact of KMS key rotation on the application.

4. **Team Involvement:**
   - **Biplatform Team**
     - Responsible for coordinating the activity.
   - **CloudOps Team**
     - Conduct the KMS key rotation activity.
   - **Backup Team**
     - Initiate backup procedures before and after the activity.

5. **Team Responsibilities:**
   - **CloudOps Team:**
     - Perform KMS key rotation activity following best practices.
   - **Backup Team:**
     - Take application backup before the activity.
     - Create a snapshot of the instance before the activity, retaining it for more than 15 days.
   - **Biplatform Team:**
     - Conduct application testing before and after the activity to ensure proper functionality.

6. **Downtime:**
   - **DEV:** 1 hour downtime expected.
   - **UAT:** 1 hour downtime expected.
   - **Prod:** 3 hours downtime expected.

7. **Backup Plan:**
   - Take application backup before initiating the activity to ensure data integrity.
   - Coordinate with the Backup team to take a snapshot of the instance before the activity to minimize data loss.

[Include any additional details or considerations specific to your environment or requirements.]

By following this activity plan, we aim to ensure a smooth and secure rotation of KMS keys with minimal impact on the application and services. Please review and coordinate accordingly.

[Your Name]  
[Your Contact Information]
