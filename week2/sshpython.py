from netmiko import ConnectHandler
from getpass import getpass
import time

cisco4 = {

	"host": 'cisco4.lasthop.io',
	"username": 'pyclass',
	"password": getpass(),
	"secret": '88newclass',
	"device_type": 'cisco_ios',
	"session_log": 'sshpython_log.txt',
}

net_connect = ConnectHandler(**cisco4)


print("\nCurrent prompt: ")
output = net_connect.find_prompt()
print(output)

print("\nConfig t prompt")
output = net_connect.config_mode()
print(output)

print("\nExit config mode")
output = net_connect.exit_config_mode()
print(output)

print("\nExit Exec priviledge mode")
net_connect.write_channel("disable\n")
time.sleep(2)
output = net_connect.read_channel()
print(output)

print("\nRe Enter enable mode")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()

print("Your are done bro")



