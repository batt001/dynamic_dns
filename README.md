# YDNS update python script

Script for updating the IP address attached to ydns.io hostname.

This script uses the services provided by ydns.io.


To autostart the service at system startup add the following lines to your /etc/rc.local file (change the scripts path obviously):

```
/bin/bash /home/osmc/dynamic_dns/dynamic_dns_process.sh status | grep "Dynamic DNS process is not running..."
if [ "$?" -eq 0 ]
then
    /bin/bash /home/osmc/dynamic_dns/dynamic_dns_process.sh start
fi
```
