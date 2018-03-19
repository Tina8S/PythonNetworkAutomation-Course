#!/usr/bin/env python

import json
import yaml
from pprint import pprint as pp

my_list = list(range(8))
my_list.append({})
my_list[-1]["attrib1"] = "something"
my_list[-1]["attrib2"] = "something else"
my_list[-1]["attrib3"] = list(range(3))

print(my_list)

with open("yamldump.yml", "w") as y:
    yaml.dump(my_list, y)

with open ("jsondump.json", "w") as j:
    json.dump(my_list, j)

y.close()
j.close()

with open ("yamldump.yml", "r") as yr:
    my_yaml = yaml.load(yr)
    pp(my_yaml)

with open ("jsondump.json", "r") as jr:
    my_json = json.load(jr)
    pp(my_json)
