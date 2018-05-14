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

print(nxos1.show('show hostname'))
print(nxos2.show('show hostname'))


