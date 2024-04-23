Here's a template for a Confluence page based on the details you provided:

---

# Setting Up BACE Microservice on Apache Tomcat

## Introduction
This guide outlines the steps to set up the BACE Microservice on Apache Tomcat.

## Steps

### 1. Check Tomcat Installation Directory
After installing Apache Tomcat, navigate to the installation directory:
```
/opt/tomcat/
```

### 2. Verify Directory Contents
Confirm the presence of multiple directories inside `/opt/tomcat/`.

### 3. Validate Files
Ensure that the necessary files are present in the directories. If not, download them from the official Apache website.

### 4. Deploy BACE Microservice
Navigate to the `webapps` folder and deploy the `BACE-Microservice.war` file.

### 5. Change Ownership
Change the ownership of the directories inside `/opt/tomcat` from root user to tomcat user:
```
sudo chown -R tomcat:tomcat /opt/tomcat
```

### 6. Update Application Properties
Edit the `application.properties` file located at:
```
/opt/tomcat/webapps/BACE-Microservice/WEB-INF/classes
```
Update the details as per the provided file.

### 7. Restart Tomcat
Restart the Apache Tomcat service:
```
sudo systemctl restart tomcat
```

### 8. Verify Deployment
Access the website by navigating to `<ip_address>:9090` in your web browser. The website should now be up and running.

---

You can copy and paste this template into a new Confluence page and fill in any specific details or instructions as needed.
