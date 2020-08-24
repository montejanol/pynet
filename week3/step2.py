import yaml

cisco3 = {"device_name": "cisco3", "host_name": "cisco3.lasthop.io"}
cisco4 = {"device_name": "cisco4", "host_name": "cisco4.lasthop.io"}
arista1 = {"device_name": "arista1", "host_name": "arista1.lasthop.io"}
arista2 = {"device_name": "arista2", "host_name": "arista2.lasthop.io"}


dictionary = [cisco3, cisco4, arista1, arista2]

for my_devices in dictionary:
    my_devices["Username"] = "admin"
    my_devices["Password"] = "cisco"

print(dictionary)

with open("yaml.yml", "w") as f:
        yaml.dump(dictionary, f, default_flow_style=False)

