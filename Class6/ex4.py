#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

vars = {
    'contact': 'Isaak Newton',
    'location': 'San Francisco, CA',
    'community': 'foo'
}

template_file = "arista_template.j2"
template = env.get_template(template_file)
rendered_output = template.render(**vars)
print(rendered_output)
