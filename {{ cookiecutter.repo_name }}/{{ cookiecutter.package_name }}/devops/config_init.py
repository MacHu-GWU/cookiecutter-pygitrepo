# -*- coding: utf-8 -*-

"""
Read config values based on the current environment name.
"""

from os.path import dirname, join

from configirl import read_text, json_loads

from .config import Config

dir_project_root = dirname(dirname(dirname(__file__)))
shared_config_file = join(dir_project_root, "config", "00-config-shared.json")
env_config_file = join(dir_project_root, "config", "config-raw.json")

config = Config()
config.update(
    json_loads(read_text(shared_config_file))
)
config.update(
    json_loads(read_text(env_config_file))
)

# Read additional config data from external store.
# put your code here ...
