#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from pynxos.device import Device
from getpass import getpass
from pprint import pprint as pp

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nxos1 = Device(host='nxos1.twb-tech.com',
               username='pyclass',
               password=getpass(),
               transport='https',
               port='8443')

nxos2 = Device(host='nxos2.twb-tech.com',
               username='pyclass',
               password=getpass(),
               transport='https',
               port='8443')

command = "show ip route vrf management"
output = nxos1.show(command)

routes = output['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix']
for route in routes:
    if route['ipprefix'] == '0.0.0.0/0':
        print(route['TABLE_path']['ROW_path']['ipnexthop'])
