#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

ospf_networks = [
    {'network': '10.220.88.0', 'wildcard': '0.0.0.255', 'area': 0},
    {'network': '172.31.255.28', 'wildcard': '0.0.0.0', 'area': 1},
]

vars = {
    'process_id': 40,
    'ospf_networks': ospf_networks,
    'loopback0_addr': '172.31.255.1',
    'loopback0_mask': '255.255.255.255'
}

template_file = "ospf_config_for.j2"
template = env.get_template(template_file)
rendered_output = template.render(**vars)
print(rendered_output)
