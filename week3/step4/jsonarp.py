import json
from pprint import pprint

filename = "jsonarp.json"
with open(filename) as f:
    arp_data = json.load(f)


arp_dict = {}

arp_entries = arp_data["ipV4Neighbors"]

for entries in arp_entries:
	ipv4_address = entries["address"]
	mac_address = entries["hwAddress"]
	arp_dict[ipv4_address] = mac_address

pprint(arp_dict)
 


