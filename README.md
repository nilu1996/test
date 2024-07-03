Need to create Infra to support scalable architecture for Tableau Screenshot Export service for BI Platform using AWS Sandbox environment. 

SharePoint Reference for System Architecture Design:

BI Tableau Screenshot Export.png

Attached the image also below.




Checklist:

API Gateway connectivity
Lambda service to validate API Key and Secrets
AWS SQS to support Queue mechanism
AWS Lambda service to pull request from the SQS and process the request
Email Trigger Service upon success/failure.
Need logger implementation (services logs should be added to S3 - So that ELK can pull the logs through it) . IN GBT we are using ELK to logs streaming) 


