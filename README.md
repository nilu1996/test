/tmp/automated-installer -a tsmadmin -f /tmp/config.json -r /tmp/registration.json -s /tmp/secrets.properties TSRX-8C86-1230-CAB3-DA4F -v --accepteula --force /tmp/tableau-server.rpm
  438  /tmp/automated-installer -a tsmadmin -f /tmp/config.json -r /tmp/registration.json -s /tmp/secrets.properties -k TSRX-8C86-1230-CAB3-DA4F -v --accepteula --force /tmp/tableau-server.rpm
  439  source /etc/profile.d/tableau_server.sh
  440  tsm status
  441  tsm stop
  442  tsm topology nodes get-bootstrap-file --file /tmp/bootstrap.json
  443  aws s3 cp /tmp/bootstrap.json s3://gbt-tableaubucket/dev-tsm-backups/bootstrap.json
  444  tsm topology external-services repository enable -f /tmp/rdsconfig.json --no-ssl
  445  cd /tmp/
  446  ls
  447  cat rdsconfig.json
  448  tsm topology external-services repository enable -f /tmp/rdsconfig.json --no-ssl
  449  tsm topology external-services repository enable -f /tmp/rdsconfig.json --no-ssl
  450  cd /tmp/
  451  ls
  452  vi rdsconfig.json
  453  tsm topology external-services repository enable -f /tmp/rdsconfig.json --no-ssl
  454  tsm status -v
  462  curl localhost
  463  systemctl status firewalld
  464  iptables -l
  465  clear
  466  tsm licenses deactivate -k TSRX-8C86-1230-CAB3-DA4F
  468  /tmp/automated-installer -a tsmadmin -f /tmp/config.json -r /tmp/registration.json -s /tmp/secrets.properties -k TSRX-8C86-1230-CAB3-DA4F -v --accepteula --force /tmp/tableau-server.rpm
  470  tsm status
  471  source /etc/profile.d/tableau_server.sh
  472  tsm stop
  473  tsm topology nodes get-bootstrap-file --file /tmp/bootstrap.json
  474  aws s3 cp /tmp/bootstrap.json s3://gbt-tableaubucket/dev-tsm-backups/bootstrap.json
  475  tsm topology external-services repository enable -f /tmp/rdsconfig.json --no-ssl
  476  tsm start
  478  clear
  479  curl localhost
  480  tsm status
  481  tsm licenses list

