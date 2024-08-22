1.  tsm stop
2.  Take snapshot from external RDS DB
3.  Launch with storage enrcypted RDS 
    https://dev.to/aws-builders/how-to-encrypt-an-unencrypted-rds-db-instance-262g
	
	Follow link for RDS snapshot change
4.  Run the following TSM CLI command to move the repository to a specific node:

    tsm topology external-services repository disable -n node1
	
	Note : Help if anything need to be changed in above specific command.
	
5. Move local repository to external:
   Create json file :
 {
 "flavor":"rds",
 "masterUsername":"rails",
 "masterPassword":"tsmDBpass#2023", 
 "host":"tsm-dev-stack-3-rdsinstance-nvsdehq2ewzm.cwicosnm4qi7.us-east-1.rds.amazonaws.com",
 "port":5432
}

6. tsm topology external-services repository enable -f file.json -c <ssl certificate file>.pem

   I guess we dont used encrypted connection between tableau server to RDS becasuse if we run 
   
   tsm configuration get -k pgsql.ssl.enabled
   I am getting responce false here. 
   
   So expected is command shoudl be:
