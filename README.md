  rmtadmin create-env --name=production --api-username=tableau_admin --api-password=tableau_gbt#2024 --gateway-url https://tableau.gbt.gbtad.com --version 2023.3.0 --repository-server tsm-prod-stack-rdsinstance-1m07to2nzls3.ctycrxiwiiam.us-east-1.rds.amazonaws.com 
   
   
   rmtadmin create-env --name=production --api-username=tableau_admin --api-password=tableau_gbt#2024
   
   
   
"flavor":"rds",
"masterUsername":"rails",
"masterPassword":"tsmDBpass#2023",
"host":" tsm-prod-stack-rdsinstance-1m07to2nzls3.ctycrxiwiiam.us-east-1.rds.amazonaws.com",
"port":5432


Options:
      --non-interactive      Disable all interactive prompts.
      --no-test              Disable testing API and repository connections.
      --name=VALUE           Name of the environment.
      --id=VALUE             System generated Identifier of the environment
                               used in web interface URLs.
      --gateway-url=VALUE    URL used to access the Tableau Server gateway.
      --version=VALUE        Version of Tableau Server the environment is
                               currently running.
      --api-username=VALUE   User to connect to Tableau Server APIs with. The
                               user should be a Server Administrator with
                               access to all sites in Tableau Server.
      --api-password=VALUE   Password to connect to Tableau Server APIs with.
      --api-password-file=VALUE
                             File containing password to connect to Tableau
                               Server APIs with.
      --repository-server=VALUE
                             Tableau Repository server
      --repository-port=VALUE
                             Tableau Repository port number
      --repository-database=VALUE
                             Tableau Repository database name
      --repository-username=VALUE
                             Tableau Repository username
      --repository-password=VALUE
                             Tableau Repository password
      --repository-password-file=VALUE
                             File containing Tableau Repository password
      --repository-ssl-mode=VALUE
                             Tableau Repository SSL mode: PreferTls, RequireTls,
                                Disable, RequireTlsWithCAVerification,
                               RequireTlsWithFullVerification
      --repository-ssl-thumbprint=VALUE
                             Tableau Repository SSL certificate thumbprint
