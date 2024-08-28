HTTPS
As a best practice, you should use HTTPS to protect sensitive information and user credentials.

The Require HTTPS setting in the Server configuration is used for communications between the users and the RMT Server. It is also used when you register an Agent. Regular agent communications between Agent and RMT to collect data is done through Rabbit MQ.

Initially, the RMT Server is installed with a self-signed certificate and will use that certificate for HTTPS communication which includes communication during Agent registration. You can use your own certificate to replace the self-signed certificate. This can be done during RMT Server install in the Server Configuration page or after the installation is complete.

SSL Certificate Mode and Requirements
The resource monitoring tool supports the following modes of using SSL Certificates:

Default: This mode uses the default self-signed certificate supplied by the installer.
Local: This mode allows you to specify a file-based certificate in the /var/opt/tableau/tabrmt/master/config folder.
Follow these guidelines and requirements for your certificate:

You must have a HTTPS certificate (like X.509) for the appropriate domains. This depends on your local security policies and certificate requirements. For example, if the Resource Monitoring Tool is using a CName or SSL passthrough proxy then you might need to use a SAN certificate. For multiple sub-domains, wildcard certificates are supported.
The Resource Monitoring Tool supports only PKCS #12 and PEM formats.
The Resource Monitoring Tool web server requires a certificate and a private key, and optionally chain-of-trust.

The private key can be either RSA or DSA.

These can be provided in a single file or grouped files.

Single file examples:
PKCS #12: A single file with the .pfx or .p12 file extensions.
PEM: PEM-encoded certificate + private key (plus optionally intermediate CAs chaining up to root CA), in a single file with the .pem extension. The items in the file does not have to be in any specific order.
Grouped file examples:
PEM-encoded certificate in a .crt or .cer file PLUS
PEM-encoded private key in a .key file PLUS (optionally)
PEM-encoded certificate authority in one or more .ca files
Default File and Directory locations:
