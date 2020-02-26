# -*- coding: utf-8 -*-

"""
Read config values based on the current environment name.
"""

import os
from os.path import dirname, join

from configirl import read_text, json_loads

from .config import Config

dir_project_root = dirname(dirname(dirname(__file__)))
shared_config_file = join(dir_project_root, "config", "00-config-shared.json")
shared_secret_config_file = join(dir_project_root, "config", "00-config-shared-secrets.json")
env_config_file = join(dir_project_root, "config", "config-raw.json")

config = Config()

# circleci container runtime
if config.is_circle_ci_runtime():
    config.update(json_loads(read_text(shared_config_file)))
    config.update(json_loads(read_text(env_config_file)))
    config.AWS_ACCOUNT_ID.set_value(os.environ["AWS_ACCOUNT_ID"])
# aws lambda runtime
elif config.is_aws_lambda_runtime():
    config.update_from_env_var(prefix="PYGITREPO_")
# local runtime
else:
    config.update(json_loads(read_text(shared_config_file)))
    config.update(json_loads(read_text(shared_secret_config_file)))
    config.update(json_loads(read_text(env_config_file)))

# Read additional config data from external store.
# put your code here ...
