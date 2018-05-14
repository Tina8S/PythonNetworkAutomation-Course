#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import jinja2


with open("ospf_config.j2") as f:
    ospf_config = f.read()

vars = {
    'process_id': 40,
    'network': '10.220.88.0',
    'wildcard': '0.0.0.255',
    'area': 0,
    'loopback0_addr': '172.31.255.1',
    'loopback0_mask': '255.255.255.255'
}

template = jinja2.Template(ospf_config)
rendered_output = template.render(**vars)
print(rendered_output)
