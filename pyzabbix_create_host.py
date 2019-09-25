from pyzabbix import ZabbixAPI
import os

zapi = ZabbixAPI('http://127.0.0.1')  ## Ip address of zabbix server
zapi.session.verify = False
api_auth_token = zapi.login('Admin', 'zabbixpass')	## Admin is sample username of zabbix server, zabbixpass is the sample password.
zapi.user.get(userids=-1)


csvfile = open('list.csv', 'r')		## Here you may change name of CSV file


def get_hostgroup_id(hostgroup):
	data = zapi.hostgroup.get(filter={'name': hostgroup})
	if data != []:
		hostgroupid = data[0]['groupid']
	else:
		raise Exception('Could not find hostgroupID for: ' + hostgroup)
	return str(hostgroupid)
	
	
def add_host(ip, hostname, hostgroups):
	interface_list = [{
		"type": 1,
		"main": 1,
		"useip": 1,
		"ip": str(ip),
		"dns": '',
		"port": "10050"
	}]

	groups = list()

	for g in hostgroups:
		groups.append({"groupid": str(get_hostgroup_id(g))})


	query = {
		'host': str(hostname),
		'groups': groups,
		'proxy_hostid': '0',
		'status': '0',
		'interfaces': interface_list,
		'inventory_mode': 1,
		'inventory': {
			'name': str(hostname)
		}
		}

	result = zapi.host.create(**query)


for l in csvfile.readlines():
	if l.strip().startswith('#') or not ',' in l:
		continue

	myargs = l.strip().split(',')
	try:
		add_host(myargs[0], myargs[1], myargs[2].split(':'))
		print("Added %s" %myargs[0])
	except:
		print("Failed to add %s" %myargs[0])
		pass








