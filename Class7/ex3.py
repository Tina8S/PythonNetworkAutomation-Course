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

pynet_rtr1_conn.open()

bgp_neighbors = pynet_rtr1_conn.get_bgp_neighbors()
pp(bgp_neighbors)

def bgp_neighbor(bgp_data, neighbor):
    return bgp_data['global']['peers'][neighbor]

neighbor = '10.220.88.38'

is_up = bgp_neighbor(bgp_neighbors, neighbor)['is_up']

print("BGP Neighbor: {}, BGP State: {}".format(neighbor, is_up))
