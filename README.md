Here’s a sample Confluence page layout for documenting your CloudFormation Template (CFT) setup with the additional worker node for Tableau. You can fill in the details as required:

---

## **Adding an Extra Worker Node for Tableau Using CloudFormation**

This document describes the steps taken to add a new worker node (Worker Node 2) in Tableau using CloudFormation (CFT). The configuration for Worker Node 2 is based on the existing Worker Node 1 configuration.

---

### **Overview**

- **Purpose**: To scale the Tableau environment by adding a new worker node (Worker Node 2) using CloudFormation.
- **Original Setup**: Single worker node (Worker Node 1).
- **New Setup**: Adds a second worker node (Worker Node 2) with the same configuration as Worker Node 1.

---

### **CloudFormation Template (CFT) Overview**

- **Template Name**: ""
- **Template Location (S3 or other)**: ""
- **Parameters Used**:
  - **Worker Node 1 Configuration**: ""
  - **Worker Node 2 Configuration**: Same as Worker Node 1

---

### **Key Changes Made in the CFT**

1. **Worker Node 2 Configuration**:  
   Copied the configuration of Worker Node 1 and modified the following:
   - **Instance Type**: ""
   - **Subnet**: ""
   - **Security Group**: ""
   - **Elastic Load Balancer (if applicable)**: ""

2. **Auto Scaling Configuration (if applicable)**:  
   - **Auto Scaling Group Name**: ""
   - **Desired Capacity**: ""

---

### **IAM Roles and Policies**

- **Role for Worker Node 1**: ""
- **Role for Worker Node 2**:  
  Copied from Worker Node 1:
  - **Role Name**: ""
  - **Policy Attached**: ""

---

### **Networking**

- **VPC ID**: ""
- **Subnets**: ""
  - Worker Node 1: ""
  - Worker Node 2: ""
- **Security Groups**:
  - Worker Node 1: ""
  - Worker Node 2: ""

---

### **Tableau Server Configuration**

- **Primary Node**: ""
- **Worker Node 1**: ""
  - CPU: ""
  - Memory: ""
  - Services Running: ""
  
- **Worker Node 2**:  
  Configured identically to Worker Node 1:
  - CPU: ""
  - Memory: ""
  - Services Running: ""

---

### **Load Balancer Configuration (if applicable)**

- **Load Balancer Type**: ""
- **Load Balancer Listener**: ""
- **Target Group**: ""
- **Health Check Settings**: ""

---

### **Steps to Deploy**

1. **Upload the CloudFormation Template**:  
   - Location: ""

2. **Launch CloudFormation Stack**:
   - Stack Name: ""
   - Parameters Filled:
     - Worker Node 1: ""
     - Worker Node 2: ""
   
3. **Monitor Stack Creation**:
   - Check for successful creation of both Worker Nodes.

4. **Verify Tableau Configuration**:
   - Ensure Worker Node 2 is correctly added to the Tableau Server cluster.
   - Services running on Worker Node 2: ""

---

### **Testing and Validation**

- **Tableau Server Status**:
  - Primary Node: ""
  - Worker Node 1: ""
  - Worker Node 2: ""
- **Validation Steps**:
  - Ensure that Worker Node 2 is functioning correctly by checking:
    - CPU/Memory usage: ""
    - Tableau Server logs: ""
    - Connectivity to the primary node: ""

---

### **Future Improvements**

- Consider using **Auto Scaling** for better management of worker nodes based on demand.
- Explore the use of **CloudWatch** for better monitoring and alerting for worker nodes.

---

This Confluence page can be updated with more details as you finalize the configurations and successfully deploy the additional worker node.
