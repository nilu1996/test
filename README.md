**Configuring SAML Authentication for Tableau Server with Okta**

---

### Before You Begin:

1. **Export IdP Metadata XML:**
   - Go to your IdP’s website or application and export the IdP’s metadata XML file.
   - Confirm that the metadata XML includes a SingleSignOnService element with binding set to HTTP-POST.

2. **Gather Certificate Files:**
   - Obtain the certificate files required for SAML authentication from your IdP.
   - Place these certificate files on the Tableau Server.

3. **Create SAML Folder on Tableau Server:**
   - Create a new folder named "SAML" in the Tableau Server directory.
   - Place copies of the SAML certificate files in this folder.

### Step 1: Configure SAML Settings on Tableau Server:

- Open the command prompt shell and run the following command to configure SAML settings (replace placeholder values with actual paths and filenames):
   ```
   tsm authentication saml configure --idp-entity-id https://tableau-server --idp-metadata "C:\Program Files\Tableau\Tableau Server\SAML\<metadata-file.xml>" --idp-return-url https://tableau-server --cert-file "C:\Program Files\Tableau\Tableau Server\SAML\<file.crt>" --key-file "C:\Program Files\Tableau\Tableau Server\SAML\<file.key>"
   ```

- If using a protected PKCS#8 key, set the passphrase:
   ```
   tsm configuration set -k wgserver.saml.key.passphrase -v <passphrase>
   ```

- Enable SAML authentication if not already enabled:
   ```
   tsm authentication saml enable
   ```

- Apply changes:
   ```
   tsm pending-changes apply
   ```

### Step 2: Generate Tableau Server Metadata and Configure IdP:

- Run the command to generate the required XML metadata file for Tableau Server:
   ```
   tsm authentication saml export-metadata -f <file-name.xml>
   ```

- On your IdP’s website or application, add Tableau Server as a Service Provider and import the generated metadata file.

### Step 3: Match Assertions (if needed):

- Ensure that assertion values in Tableau Server configuration match those passed by your IdP.
- Use the provided table to map assertion values accordingly.

### Optional Steps:

- **Disable Client Types from Using SAML:**
  ```
  tsm authentication saml configure --desktop-access disable
  tsm authentication saml configure --mobile-access disable
  tsm pending-changes apply
  ```

- **Add AuthNContextClassRef Value:**
  ```
  tsm configuration set -k wgserver.saml.authcontexts -v <value>
  tsm pending-changes apply
  ```

### Conclusion:

By following these steps, you can successfully configure SAML authentication for Tableau Server with Okta as the Identity Provider. Ensure thorough testing and monitoring to ensure a smooth authentication experience for users accessing Tableau Server.

--- 

Feel free to customize the steps further based on your specific environment and requirements!
