import os
from pprint import pprint
from netmiko import ConnectHandler, file_transfer
from getpass import getpass


nxos1 = {

	"host": 'nxos1.lasthop.io',
	"username": 'pyclass',
	"password": '88newclass',
	"device_type": 'cisco_nxos',
}

nxos2 = {

	"host": 'nxos2.lasthop.io',
	"username": 'pyclass',
	"password": '88newclass',
	"device_type": 'cisco_nxos',

}




for switches in (nxos1, nxos2):

	net_connect = ConnectHandler(**switches)
	output = net_connect.send_config_from_file("vlans.txt")
	print(output)
	net_connect.save_config()
	net_connect.disconnect()




