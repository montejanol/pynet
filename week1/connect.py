from netmiko import ConnectHandler
from getpass import getpass

password = getpass()




nxos1 = {

	"host": 'nxos1.lasthop.io',
	"username": 'pyclass',
	"password": password,
	"device_type": 'cisco_ios',
	# session_log='my_session.txt',
}

nxos2 = {

	"host": 'nxos2.lasthop.io',
	"username": 'pyclass',
	"password": password,
	"device_type": 'cisco_ios',
}


counter = 0

for device in [nxos1, nxos2]:
	

	if (counter <1):
		net_connect = ConnectHandler(**device)
		intBrief = net_connect.send_command("show version")
		print(net_connect.find_prompt() + "\n")
		print(intBrief)
	else:
		with open("show_version_nxos2.txt", "w") as f:
			f.write(intBrief)
		net_connect.disconnect()
	counter = counter + 1


		



