import json

filename = "step3addressing.json"
with open(filename) as f:
    nxos_data = json.load(f)

ipv4_list = []
ipv6_list = []
ipv4_counter = 0


for interface , ipadd_dict in nxos_data.items():
	for ipv4_or_ipv6, addr_info in ipadd_dict.items():
		for ipaddr, prefix_dict in addr_info.items():
			prefix_length = prefix_dict["prefix_length"]
			#print(prefix_length)
			if ipv4_or_ipv6  == "ipv4":
				ipv4_list.append("{}/{}".format(ipaddr, prefix_length))
			else:
				ipv6_list.append("{}/{}".format(ipaddr, prefix_length))
print (ipv4_list)
print (ipv6_list)


