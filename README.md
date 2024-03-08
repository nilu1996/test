Alteryx to OKTA Integration
Overview
This document outlines the steps required to integrate Alteryx with OKTA for authentication purposes.

Steps
Raise Ticket Request

Raise a ticket request to the IAM team requesting the creation of metadata required for integration.
Reference Ticket: [Insert Ticket Number]
Receive Metadata URL

Upon receiving the metadata, note the URL provided. Append "/metadata" at the end.
Metadata URL: [Insert URL]
Network Accessibility Check

Verify if the provided URL is allowed in the GBT network.
Raise Firewall Ticket (If Necessary)

If the URL is not accessible within the GBT network, raise a firewall ticket to allow access.
Firewall Ticket: [Insert Ticket Number]
Access Alteryx Windows Server

Open Alteryx Settings Dialog Box

Navigate to SAML Configuration Page

In the IDP Meta section, specify the metadata URL.
In the Metadata section, specify the metadata URL.
Verify IDP Connection

Click on the "Verify IDP" button to initiate the connection verification process.
Enter Credentials and Test Connection

Enter the required credentials and test the connection.
Complete Configuration

Click on "Next" until the configuration process is finished. This will restart the
