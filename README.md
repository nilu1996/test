Hello Nilesh 

This Karabo here again, Thank you for connecting with me earlier. 

During the call we successfully built a customer container and attached it to the domain, however, we were not able to start the notebook using the custom image due to a 400 Bad Request error.

I would like to inform you that your JupyterLab fails to launch with a custom image due to  status code  400 Bad Request returned when trying to connect to SageMaker API endpoint. When you click on "Run Space" Studio tries to first update the space image using the UpdateSpace API. From the HAR file you shared, it failed to send a UpdateSpace request to the SageMaker endpoint "api.sagemaker.us-east-1.amazonaws.com" with a 400 Bad Request status code.

I reviewed the VPC "vpc-0e86f92aeebe0b3b2" used by your domain and could not locate the SageMaker API endpoint "com.amazonaws.region.sagemaker.api". I would like to inform you that your domain is deployed in VPC only mode. In order to call the UpdateSpace API you will need the SageMaker api endpoint "com.amazonaws.region.sagemaker.api". To learn more about VPC only requirements please see this link [1]. 

To create a VPC endpoint please follow this link [2]. Your domain was created using this subnet "subnet-09997d8d032494830" and this security group: "sg-0bfc83c5dd1872949". Please use this same subnet and security group when creating the endpoint.  

After you create the endpoint, please try launching again. If you encounter any issues, we will be happy to schedule a call to troubleshoot.

Please let me know if you have any other questions. I'm here to assist you.

References: 
[1] https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html 
[2]  https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html 

We value your feedback. Please share your experience by rating this and other correspondences in the AWS Support Center. You can rate a correspondence by selecting the stars in the top right corner of the correspondence.

Best regards,
Karabo K.
Amazon Web Services
