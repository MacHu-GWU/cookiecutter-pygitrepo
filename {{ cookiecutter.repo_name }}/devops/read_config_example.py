# -*- coding: utf-8 -*-

"""
This is an example about how to read configs for your DevOps automation.

To read config values from file or external systems, first you need to
switch to a environment (dev / test / prod) using ``./config/switch-env dev``
in cli. Then import the ``config_init`` script that reads values from json
file and external systems.
"""

from {{ cookiecutter.package_name }}.devops.config_init import config

print(config)
