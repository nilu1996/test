[Unit]
Description=Apache Tomcat Web Application Container
After=syslog.target network.target

[Service]
Type=forking
Environment=JAVA_HOME=/usr/bin
Environment=CATALINA_HOME=/opt/tomcat/apache-tomcat-9.0.85-src
ExecStart=/opt/tomcat/apache-tomcat-9.0.85-src/bin/startup.sh
ExecStop=/opt/tomcat/apache-tomcat-9.0.85-src/bin/shutdown.sh
User=tomcat
Group=tomcat
Restart=on-failure

[Install]
WantedBy=multi-user.target


