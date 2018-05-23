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

driver = get_network_driver('eos')

arista_sw2_conn = driver(devices['pynet-sw2']['hostname'], devices['pynet-sw2']['username'], devices['pynet-sw2']['password'], optional_args = devices['pynet-sw2']['optional_args'])

arista_sw2_conn.open()

interfaces = arista_sw2_conn.get_interfaces()
pp(interfaces)

def int_state(int_data, int):
    return int_data[int]['is_enabled'], int_data[int]['is_up']

for i in interfaces:
    if int_state(interfaces, i) == (True, True):
        print(i)



