import re

from Manager import Manager


# m = Manager('./custom_nodes')

patten = r"([a-zA-Z0-9_.]+)+(<=|<|>=|>|==|!=)*([\d.]+)*"
match = re.match(patten, "pack1==1.1.1")
print(match)
print(match.group(0))