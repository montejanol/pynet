from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

nxos2 = {

	"host": 'nxos2.lasthop.io',
	"username": 'pyclass',
	"password": getpass(),
	"device_type": 'cisco_ios',
	"global_delay_factor": 2,
}

cmd = "show lldp neighbors detail"

net_connect = ConnectHandler(**nxos2)
start_time = datetime.now()
output1 = net_connect.send_command(cmd)
end_time = datetime.now()

print(output1)
print("\n" * 3)

print(start_time)
print(end_time)
print (end_time - start_time)
print("#" * 80)


start_time = datetime.now()
output2= net_connect.send_command(cmd, delay_factor = 8)
end_time = datetime.now()

print(output1)
print("\n" * 3)
print(start_time)
print(end_time)
print (end_time - start_time)
print("#" * 80)
