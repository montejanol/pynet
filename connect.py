from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {

	"host": 'nxos1.lasthop.io',
	"username": 'pyclass',
	"password": getpass(),
	"device_type": 'cisco_ios',
	# session_log='my_session.txt',
}




net_connect = ConnectHandler(**nxos1)
intBrief = net_connect.send_command("show ip int brief")


print(net_connect.find_prompt())

print(intBrief)


