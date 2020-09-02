import re

string = '192.168.1.1'

search = re.search(r"(\S+)", string).group(1)

print (search)

