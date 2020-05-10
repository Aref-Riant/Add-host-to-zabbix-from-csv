# Add-host-to-zabbix-from-csv
Simple python script to add new hosts to zabbix from CSV file.

This is a simple python script which reads a csv files and adds hosts to zabbix monitoring server.

## How to use it?
1. Edit CSV file as you need:
  csv file has three columns: IP address, hostname(the host name you want to set in zabbix server), hostgroups(you can add many, delimited by ':' sign).
  
2. Edit 'pyzabbix_create_host.py' file:
      in the beginning of file, you can set credentials of zabbix server, and you may change path of csv file.

3. Run the script:
   the only dependancy is 'pyzabbix' package which you could install with coammnd: 'pip install pyzabbix'
   then you could simply run the script like this: "python pyzabbix_create_host.py"
