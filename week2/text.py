from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass


device1 = {

	"host": 'cisco4.lasthop.io',
	"username": 'pyclass',
	"password": '88newclass',
	"device_type": 'cisco_ios',
}



net_connect = ConnectHandler(**device1)

output = net_connect.send_command("show lldp neighbors", use_textfsm=True)
pprint(output[0]['neighbor_interface'])
output = net_connect.send_command("show version", use_textfsm=True)
pprint(output)


