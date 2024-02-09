09-Feb-2024 06:38:17.222 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Command line argument: -Dcatalina.base=/usr/share/tomcat
09-Feb-2024 06:38:17.222 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Command line argument: -Dcatalina.home=/usr/share/tomcat
09-Feb-2024 06:38:17.222 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Command line argument: -Djava.endorsed.dirs=
09-Feb-2024 06:38:17.222 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Command line argument: -Djava.io.tmpdir=/var/cache/tomcat/temp
09-Feb-2024 06:38:17.222 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Command line argument: -Djava.util.logging.config.file=/usr/share/tomcat/conf/logging.properties
09-Feb-2024 06:38:17.223 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Command line argument: -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager
09-Feb-2024 06:38:17.224 INFO [main] org.apache.catalina.core.AprLifecycleListener.lifecycleEvent The Apache Tomcat Native library which allows using OpenSSL was not found on the java.library.path: [/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib]
09-Feb-2024 06:38:17.433 INFO [main] org.apache.coyote.AbstractProtocol.init Initializing ProtocolHandler ["http-nio-8080"]
09-Feb-2024 06:38:17.448 INFO [main] org.apache.catalina.startup.Catalina.load Server initialization in [354] milliseconds
09-Feb-2024 06:38:17.473 INFO [main] org.apache.catalina.core.StandardService.startInternal Starting service [Catalina]
09-Feb-2024 06:38:17.473 INFO [main] org.apache.catalina.core.StandardEngine.startInternal Starting Servlet engine: [Apache Tomcat/9.0.62]
09-Feb-2024 06:38:17.479 INFO [main] org.apache.coyote.AbstractProtocol.start Starting ProtocolHandler ["http-nio-8080"]
09-Feb-2024 06:38:17.495 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in [46] milliseconds
09-Feb-2024 06:39:07.619 INFO [http-nio-8080-exec-3] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
 Note: further occurrences of HTTP request parsing errors will be logged at DEBUG level.
        java.lang.IllegalArgumentException: Invalid character found in method name [0x160x030x010x020x000x010x000x010xfc0x030x03N0xb80xef0xa5G'Z"0x1dD:0xd90x91>0x0e<|0xa60xa35`0x960xb90x9c0xb70xa3}0xee0x8c0x0fr0x9f ]. HTTP method names must be tokens
                at org.apache.coyote.http11.Http11InputBuffer.parseRequestLine(Http11InputBuffer.java:419)
                at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:271)
                at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
                at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:890)
                at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1743)
                at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
                at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
                at java.lang.Thread.run(Thread.java:750)
09-Feb-2024 06:39:07.619 INFO [http-nio-8080-exec-4] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
 Note: further occurrences of HTTP request parsing errors will be logged at DEBUG level.
        java.lang.IllegalArgumentException: Invalid character found in method name [0x160x030x010x02:0x010x000x0260x030x030xb00x1dd0x8d0x8e0x142eE0x9aZ0x140x1f0x080x030xa60x82@O!0x820x7fI0xb60x170xc10x9e0xc20x1f0xa60xb5} ]. HTTP method names must be tokens
                at org.apache.coyote.http11.Http11InputBuffer.parseRequestLine(Http11InputBuffer.java:419)
                at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:271)
                at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
                at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:890)
                at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1743)
                at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
                at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
                at java.lang.Thread.run(Thread.java:750)
09-Feb-2024 07:04:39.344 INFO [Thread-3] org.apache.coyote.AbstractProtocol.pause Pausing ProtocolHandler ["http-nio-8080"]
09-Feb-2024 07:04:39.347 INFO [Thread-3] org.apache.catalina.core.StandardService.stopInternal Stopping service [Catalina]
09-Feb-2024 07:04:39.348 INFO [Thread-3] org.apache.coyote.AbstractProtocol.stop Stopping ProtocolHandler ["http-nio-8080"]
09-Feb-2024 07:04:39.352 INFO [Thread-3] org.apache.coyote.AbstractProtocol.destroy Destroying ProtocolHandler ["http-nio-8080"]
