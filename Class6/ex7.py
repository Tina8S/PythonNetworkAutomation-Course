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

#nxos2 = Device(host='nxos2.twb-tech.com',
#               username='pyclass',
#               password=getpass(),
#               transport='https',
#               port='8443')

print(nxos1.show('show hostname'))

commands = [
    'interface Loopback68',
    'ip address 172.16.68.68 255.255.255.255'
]

nxos1.config_list(commands)

print(nxos1.show('show run interface loopback68', raw_text=True))


