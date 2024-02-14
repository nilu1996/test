● tomcat.service - Apache Tomcat Web Application Container
   Loaded: loaded (/etc/systemd/system/tomcat.service; disabled; vendor preset: disabled)
   Active: failed (Result: exit-code) since Wed 2024-02-14 08:38:14 UTC; 5s ago
  Process: 911190 ExecStart=/opt/tomcat/apache-tomcat-9.0.85-src/bin/startup.sh (code=exited, status=1/FAILURE)

Feb 14 08:38:14 USE1NDLAUTPYA01 systemd[1]: tomcat.service: Service RestartSec=100ms expired, scheduling restart.
Feb 14 08:38:14 USE1NDLAUTPYA01 systemd[1]: tomcat.service: Scheduled restart job, restart counter is at 5.
Feb 14 08:38:14 USE1NDLAUTPYA01 systemd[1]: Stopped Apache Tomcat Web Application Container.
Feb 14 08:38:14 USE1NDLAUTPYA01 systemd[1]: tomcat.service: Start request repeated too quickly.
Feb 14 08:38:14 USE1NDLAUTPYA01 systemd[1]: tomcat.service: Failed with result 'exit-code'.
Feb 14 08:38:14 USE1NDLAUTPYA01 systemd[1]: Failed to start Apache Tomcat Web Application Container.


