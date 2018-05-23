#!/usr/bin/env python

import yaml
from pprint import pprint as pp
from napalm import get_network_driver

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Read YAML file
with open("my_devices.yml", 'r') as stream:
    devices = yaml.load(stream)

driver = get_network_driver('ios')

pynet_rtr1_conn = driver(devices['pynet-rtr1']['hostname'], devices['pynet-rtr1']['username'], devices['pynet-rtr1']['password'], optional_args = devices['pynet-rtr1']['optional_args'])
pynet_rtr2_conn = driver(devices['pynet-rtr2']['hostname'], devices['pynet-rtr2']['username'], devices['pynet-rtr2']['password'], optional_args = devices['pynet-rtr2']['optional_args'])

routers = [pynet_rtr1_conn, pynet_rtr2_conn]

for r in routers:
    r.open()
    pp(r.get_lldp_neighbors())


