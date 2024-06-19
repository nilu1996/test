Certainly! Below is a draft of a Confluence page that outlines the plan for upgrading the Alteryx server EBS volume from AWS KMS keys to a Customer Managed Key, including the prerequisite steps.

---

# Plan for Upgrading Alteryx Server EBS Volume to Customer Managed Key

## Overview
This document outlines the plan to upgrade the Alteryx server EBS volume from AWS KMS (Key Management Service) keys to a Customer Managed Key (CMK). The upgrade aims to enhance the security and control over the encryption keys used for protecting data on the Alteryx server EBS volumes.

## Prerequisite Steps

Before proceeding with the upgrade, the following prerequisite steps must be completed:

### 1. Disable the License Key
To ensure that the Alteryx server can be stopped safely without any licensing issues, the license key needs to be disabled.

1. **Log in to the Alteryx Server Admin Interface**:
   - Access the Alteryx Server Admin Interface using your admin credentials.
   - Navigate to the **Licensing** section.

2. **Disable the License Key**:
   - Locate the active license key(s) for the Alteryx server.
   - Follow the provided instructions to disable the license key(s).

### 2. Stop the Alteryx Service
Stopping the Alteryx service is essential to ensure data integrity and to prevent any potential issues during the volume encryption upgrade.

1. **Access the Server Hosting Alteryx**:
   - Use SSH or a remote desktop connection to access the server where the Alteryx service is running.

2. **Stop the Alteryx Service**:
   - Open a terminal or command prompt on the server.
   - Execute the command to stop the Alteryx service:
     ```bash
     sudo service alteryx stop
     ```

   - Verify that the service has stopped successfully by checking the service status:
     ```bash
     sudo service alteryx status
     ```

## Upgrade Plan

### Step 1: Create Customer Managed Key (CMK)
1. **Navigate to the AWS Management Console**:
   - Open the AWS Management Console and go to the **KMS** (Key Management Service) section.

2. **Create a New CMK**:
   - Click on **Create key** and follow the wizard to create a new Customer Managed Key.
   - Configure the necessary permissions and key policies.

### Step 2: Update EBS Volume Encryption
1. **Identify the EBS Volumes**:
   - Identify the EBS volumes attached to the Alteryx server instance that need to be re-encrypted.

2. **Re-Encrypt the EBS Volumes**:
   - Detach the identified EBS volumes from the Alteryx server instance.
   - Create snapshots of the EBS volumes to ensure data backup.
   - Copy the snapshots and specify the new CMK during the copy process to re-encrypt the volumes.
   - Create new EBS volumes from the re-encrypted snapshots.

3. **Attach the New EBS Volumes**:
   - Attach the newly created EBS volumes to the Alteryx server instance.

### Step 3: Restart the Alteryx Service
1. **Start the Alteryx Service**:
   - Execute the command to start the Alteryx service:
     ```bash
     sudo service alteryx start
     ```

2. **Verify the Service Status**:
   - Ensure the service has started successfully by checking the service status:
     ```bash
     sudo service alteryx status
     ```

### Step 4: Re-enable the License Key
1. **Log in to the Alteryx Server Admin Interface**:
   - Access the Alteryx Server Admin Interface using your admin credentials.
   - Navigate to the **Licensing** section.

2. **Re-enable the License Key**:
   - Enter the license key details and re-enable the license for the Alteryx server.

## Verification and Testing
1. **Verify Data Integrity**:
   - Ensure that all data on the Alteryx server is intact and accessible.
   - Run test workflows to confirm that the Alteryx server is operating correctly.

2. **Monitor System Performance**:
   - Monitor the system performance to ensure that the server is functioning optimally after the upgrade.

## Conclusion
Following this plan will ensure a smooth and secure upgrade of the Alteryx server EBS volume encryption to a Customer Managed Key, enhancing the security and control over your data.

---

Feel free to customize and expand on this template as needed for your specific requirements and environment.
