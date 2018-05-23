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

pp(devices)

for device in devices:
    napalm_conns = []
    driver = get_network_driver(devices[device]['device_type'])
    conn = driver(devices[device]['hostname'], devices[device]['username'], devices[device]['password'], optional_args = devices[device]['optional_args'])
    napalm_conns.append(conn)
    conn.open()
    facts = conn.get_facts()
    print(facts['model'])
