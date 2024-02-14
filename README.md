[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java1.8.0
Environment=CATALINA_HOME=/opt/tomcat/apache9

ExecStart=/opt/tomcat/apache9/bin/startup.sh
ExecStop=/opt/tomcat/apache9/bin/shutdown.sh

User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
