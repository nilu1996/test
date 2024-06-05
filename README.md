 would like to inform you that your JupyterLab fails to launch with a custom image due to  status code  400 Bad Request returned when trying to connect to SageMaker API endpoint. When you click on "Run Space" Studio tries to first update the space image using the UpdateSpace API. From the HAR file you shared, it failed to send a UpdateSpace request to the SageMaker endpoint "api.sagemaker.us-east-1.amazonaws.com" with a 400 Bad Request status code.

I reviewed the VPC "vpc-0e86f92aeebe0b3b2" used by your domain and could not locate the SageMaker API endpoint "com.amazonaws.region.sagemaker.api". I would like to inform you that your domain is deployed in VPC only mode. In order to call the UpdateSpace API you will need the SageMaker api endpoint "com.amazonaws.region.sagemaker.api". To learn more about VPC only requirements please see this link [1]. 

To create a VPC endpoint please follow this link [2]. Your domain was created using this subnet "subnet-09997d8d032494830" and this security group: "sg-0bfc83c5dd1872949". Please use this same subnet and security group when creating the endpoint.  

After you create the endpoint, please try launching again. If you encounter any issues, we will be happy to schedule a call to troubleshoot.
