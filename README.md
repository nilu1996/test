t-9.0.85/webapps/ROOT] has finished in [9] ms
14-Feb-2024 10:44:50.420 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deploying web application directory [/opt/tomcat/apache-tomcat-9.0.85/webapps/docs]
14-Feb-2024 10:44:50.431 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deployment of web application directory [/opt/tomcat/apache-tomcat-9.0.85/webapps/docs] has finished in [10] ms
14-Feb-2024 10:44:50.431 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deploying web application directory [/opt/tomcat/apache-tomcat-9.0.85/webapps/examples]
14-Feb-2024 10:44:50.516 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deployment of web application directory [/opt/tomcat/apache-tomcat-9.0.85/webapps/examples] has finished in [85] ms
14-Feb-2024 10:44:50.516 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deploying web application directory [/opt/tomcat/apache-tomcat-9.0.85/webapps/host-manager]
14-Feb-2024 10:44:50.528 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deployment of web application directory [/opt/tomcat/apache-tomcat-9.0.85/webapps/host-manager] has finished in [12] ms
14-Feb-2024 10:44:50.528 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deploying web application directory [/opt/tomcat/apache-tomcat-9.0.85/webapps/manager]
14-Feb-2024 10:44:50.538 INFO [main] org.apache.catalina.startup.HostConfig.deployDirectory Deployment of web application directory [/opt/tomcat/apache-tomcat-9.0.85/webapps/manager] has finished in [10] ms
14-Feb-2024 10:44:50.540 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in [17719] milliseconds
14-Feb-2024 10:44:50.542 SEVERE [main] org.apache.catalina.core.StandardServer.await Failed to create server shutdown socket on address [localhost] and port[8005] (base port [8005] and offset [0])
        java.net.BindException: Address already in use (Bind failed)
                at java.net.PlainSocketImpl.socketBind(Native Method)
                at java.net.AbstractPlainSocketImpl.bind(AbstractPlainSocketImpl.java:387)
                at java.net.ServerSocket.bind(ServerSocket.java:390)
                at java.net.ServerSocket.<init>(ServerSocket.java:252)
                at org.apache.catalina.core.StandardServer.await(StandardServer.java:581)
                at org.apache.catalina.startup.Catalina.await(Catalina.java:864)
                at org.apache.catalina.startup.Catalina.start(Catalina.java:810)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:498)
                at org.apache.catalina.startup.Bootstrap.start(Bootstrap.java:347)
                at org.apache.catalina.startup.Bootstrap.main(Bootstrap.java:478)
14-Feb-2024 10:44:50.542 INFO [main] org.apache.coyote.AbstractProtocol.pause Pausing ProtocolHandler ["http-nio-8080"]
14-Feb-2024 10:44:50.543 INFO [main] org.apache.catalina.core.StandardService.stopInternal Stopping service [Catalina]
2024-02-14 10:44:50.550  INFO 955167 --- [           main] o.s.s.c.ThreadPoolTaskScheduler          : Shutting down ExecutorService 'taskScheduler'
2024-02-14 10:44:50.550  INFO 955167 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Shutting down ExecutorService 'applicationTaskExecutor'
2024-02-14 10:44:50.553  INFO 955167 --- [           main] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'
14-Feb-2024 10:44:50.560 WARNING [main] org.apache.catalina.loader.WebappClassLoaderBase.clearReferencesJdbc The web application [BACE-Microservice] registered the JDBC driver [org.postgresql.Driver] but failed to unregister it when the web application was stopped. To prevent a memory leak, the JDBC Driver has been forcibly unregistered.
14-Feb-2024 10:44:50.568 INFO [main] org.apache.coyote.AbstractProtocol.stop Stopping ProtocolHandler ["http-nio-8080"]
14-Feb-2024 10:44:50.570 INFO [main] org.apache.coyote.AbstractProtocol.destroy Destroying ProtocolHandler ["http-nio-8080"]
