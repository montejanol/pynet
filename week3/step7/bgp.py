from ciscoconfparse import CiscoConfParse
from pprint import pprint

bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""


bgp_obj = CiscoConfParse(bgp_config.splitlines())

bgp_peers = []

neighbors = bgp_obj.find_objects_w_parents(parentspec=r"router bgp", childspec=r"neighbor")

for neighbor in neighbors:
	_, neighbor_ip = neighbor.text.split()
	for remote in neighbor.children:
		if "remote-as" in remote.text:
			_, remote_as = remote.text.split()
	bgp_peers.append((neighbor_ip, remote_as))

pprint(bgp_peers)
	
