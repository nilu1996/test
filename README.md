 Loaded: loaded (/etc/systemd/system/tomcat.service; disabled; vendor preset: disabled)
   Active: activating (auto-restart) (Result: exit-code) since Fri 2024-02-09 07:06:06 UTC; 1s ago
  Process: 245149 ExecStart=/opt/tomcat/bin/startup.sh (code=exited, status=203/EXEC)



CREATE ROLE postgres WITH LOGIN PASSWORD 'postgres';

/home/svc_calinuser177/bison/test/BISON

psql: FATAL:  Peer authentication failed for user "postgres"

● tomcat.service - Apache Tomcat Web Application Container
   Loaded: loaded (/etc/systemd/system/tomcat.service; disabled; vendor preset: disabled)
   Active: activating (auto-restart) (Result: exit-code) since Fri 2024-02-09 09:16:23 UTC; 6s ago
  Process: 261037 ExecStart=/opt/tomcat/apache-tomcat-9.0.85-src/bin/startup.sh (code=exited, status=1/FAILURE)

Feb 09 09:16:23 USE1NDLAUTPYA01 systemd[1]: tomcat.service: Failed with result 'exit-code'.
Feb 09 09:16:23 USE1NDLAUTPYA01 systemd[1]: Failed to start Apache Tomcat Web Application Container.

