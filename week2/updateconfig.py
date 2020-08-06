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

print(net_connect.find_prompt())

output = net_connect.send_command('ping 8.8.8.8')





#cfg = 'ip name-server 1.1.1.1'
#cfg2 = 'ip name-server 2.2.2.2'
#cfg3 = 'ip domain lookup'
#output = net_connect.send_config_set(cfg)
#output += net_connect.send_config_set(cfg2)
#output += net_connect.send_config_set(cfg3)
print(output)



