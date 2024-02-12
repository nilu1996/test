1. Bison Setup Update:
   Ticket: https://amexgbt.freshservice.com/support/tickets/1346112
   Waiting tikcet approval , this is blocker for me not able moved ahed without. 
   Once tomcat is working I will start configuration changes.
   
2. Worked on 1st part of ticket: BIP-56 
   I have created python script which can monitor status of instance helth , if instance is in stop state it will send the altert mail.
   I have tested this in my personal AWS Env.
   I am trying to do same in GBT env but due to restrication to create lambda not able to proceed.
   As per suggetion by Vivek,changing the my approach now, 
   I will try to do monitoring using cloudwatch group. 
   
3. SFTP POC:
   I did this POC in my Personal Env, working as per things mention in VIDEO.
   When we do changes in S3 bucket it will reflect to server side as well, same works from server side as well.
   We need to have account in : https://app.sftpcloud.io/
   I tried to do setup in my local due admin issue, I am not able to install Openssh in laptop. 
   
4. Need approval for Tableau Prod Server Standardization:

   Server will rebooted two times, let me know what will be time and date when Linux team can perform this activity. 

   USE1NPLTSBIPD01	10.201.169.94	bi-noncde-prd-use1	Prod	sgec2-bi-noncde-prd-tableau-sg-01-use 1	sg-0813f96051bbebda2
   USE1NPLTSBIPA02	10.201.170.161	bi-noncde-prd-use1	Prod	sgec2-bi-noncde-prd-tableau-sg-01-use2	sg-0813f96051bbebda3
   USE1NPLTSBIPC03	10.201.171.96	bi-noncde-prd-use1	Prod	sgec2-bi-noncde-prd-tableau-sg-01-use3	sg-0813f96051bbebda4
   
