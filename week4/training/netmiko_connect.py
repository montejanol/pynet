from netmiko import ConnectHandler
from routerlogin import  cisco3, cisco4, arista1, arista2, arista3, arista4, srx2, nxos1, nxos2

net_connect = ConnectHandler(**arista1)
print(net_connect.find_prompt())
