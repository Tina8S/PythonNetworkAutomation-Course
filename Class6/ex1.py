#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import jinja2

ospf_config = """
router ospf {{ ospf_id }}
  network {{ network }} {{ netmask }} area {{ ospf_area }}
"""

vars = {
    'ospf_id': 40,
    'network': '10.220.88.0',
    'netmask': '0.0.0.255',
    'ospf_area': 0
}

template = jinja2.Template(ospf_config)
rendered_output = template.render(**vars)
print(rendered_output)
