import yaml
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

filename = "netmiko.yml"

with open(filename) as f:
	yaml_out = yaml.safe_load(f)

device = yaml_out["cisco4"]

net_connect = ConnectHandler(**device)
show_run = net_connect.send_command("show run")


#Cisco confparse

cisco_obj = CiscoConfParse(show_run.splitlines())
#interfaces = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"ip address")

match = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

for ipaddr in match:
	print("Interface Line: ",ipaddr.text)
	ipaddress = ipaddr.re_search_children(r"ip address")[0].text
	print("IP Address Line: ", ipaddress)




#print(match[0].children)
#print (cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address"))


