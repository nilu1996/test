https://www.oracle.com/java/technologies/downloads/#java11

tar -xzvf jdk-11.0.11_linux-x64_bin.tar.gz

sudo mv jdk-11.0.11 /usr/local/

nano ~/.bashrc

export JAVA_HOME=/usr/local/jdk-11.0.11
export PATH=$JAVA_HOME/bin:$PATH

source ~/.bashrc

java --version


Subject: Cost Analysis for Setting Up CloudWatch Dashboard for EC2 Instances

Dear [Recipient Name],

I hope this email finds you well.

I am writing to provide you with a detailed cost analysis for setting up a CloudWatch dashboard to monitor our EC2 instances, including both CPU and memory metrics, along with configuring notifications.

Components and Cost Analysis
1. EC2 Instances

Cost: Variable based on instance type, size, and region.
Details: EC2 pricing is based on instance hours, storage, and data transfer.
2. IAM Role

Cost: Free.
Details: IAM is free of charge, but charges may apply for other AWS services accessed via IAM roles.
3. CloudWatch Agent

Cost: No additional charge for the CloudWatch agent itself.
Details: Charges are incurred for the metrics collected by the agent.
4. CloudWatch Metrics

Cost: $0.30 per metric per month for custom metrics.
Details: We will be collecting 4 CPU metrics and 1 memory metric. Each metric collected incurs charges.
5. CloudWatch Dashboard

Cost: $3.00 per dashboard per month.
Details: Charges are incurred per dashboard.
6. CloudWatch Alarms

Cost: $0.10 per alarm per month.
Details: Charges apply per alarm created for CPU and memory metrics.
7. SNS (Simple Notification Service)

Cost: $0.50 per 1 million Amazon SNS requests, plus $0.06 per 100,000 notifications over HTTP/S, $0.75 per 100 notifications over SMS, and $2.00 per 100,000 email notifications.
Details: Costs depend on the number of notifications sent.
Example Cost Calculation
Assuming we have 1 EC2 instance and we monitor 4 CPU metrics and 1 memory metric, with 2 alarms set up (one for CPU and one for memory), and notifications sent via email:

EC2 Instance: Variable, depending on instance type.
IAM Role: Free.
CloudWatch Agent: Free (installation and operation).
CloudWatch Metrics:
5 metrics (4 CPU + 1 memory) * $0.30 = $1.50 per month.
CloudWatch Dashboard:
1 dashboard * $3.00 = $3.00 per month.
CloudWatch Alarms:
2 alarms * $0.10 = $0.20 per month.
SNS Notifications:
Assuming 1,000 email notifications per month.
1,000 notifications * $2.00 per 100,000 = $0.02 per month.
Total Monthly Cost:

Metrics: $1.50
Dashboard: $3.00
Alarms: $0.20
Notifications: $0.02
Estimated Total: $4.72 per month (excluding the EC2 instance cost).

Please note that this cost estimation is based on the latest AWS pricing and may vary with actual usage and region. For the most accurate cost estimations, I recommend using the AWS Pricing Calculator.

If you have any questions or need further clarification, please feel free to reach out.

Best regards,

[Your Name]
