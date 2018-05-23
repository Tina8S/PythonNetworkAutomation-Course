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

pynet_rtr2_conn = driver(devices['pynet-rtr2']['hostname'], devices['pynet-rtr2']['username'], devices['pynet-rtr2']['password'], optional_args = devices['pynet-rtr2']['optional_args'])

new_route = "ip route 1.1.42.42 255.255.255.255 10.220.88.1\n"

pynet_rtr2_conn.open()

pynet_rtr2_conn.load_merge_candidate(config=new_route)

pp(pynet_rtr2_conn.compare_config())

input("Hit any key to continue!")

pynet_rtr2_conn.discard_config()

pp(pynet_rtr2_conn.compare_config())

input("Hit any key to continue!")

pynet_rtr2_conn.load_merge_candidate(config=new_route)

pynet_rtr2_conn.commit_config()

pynet_rtr2_conn.close()
