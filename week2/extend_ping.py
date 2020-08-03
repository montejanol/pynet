from netmiko import ConnectHandler
from getpass import getpass


cisco4 = {

	"host": 'cisco4.lasthop.io',
	"username": 'pyclass',
	"password": getpass(),
	"device_type": 'cisco_ios',
	"session_log": 'extend_ping.txt',
}

net_connect = ConnectHandler(**cisco4)

output = net_connect.send_command_timing(
	"ping", strip_prompt=False, strip_command=False)

output+= net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output+= net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
output+= net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output+= net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output+= net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output+= net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output+= net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print()

print(output)



