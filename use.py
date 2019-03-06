# -*- coding: utf-8 -*-

"""
create a lambda function project for dev.
"""

from __future__ import unicode_literals
import os
import sys
from datetime import datetime, date
from cookiecutter.main import cookiecutter

here = os.path.dirname(__file__)
with open(os.path.join(here, "version.txt"), "rb") as f:
    cookiecutter_pygitrepo_version = f.read().decode("utf-8").strip()

extra_context = dict(
    package_name="learn_awslambda",
    github_username="MacHu-GWU",
    author_name="Sanhe Hu",
    author_email="husanhe@gmail.com",
    command_line_interface="No command-line interface",
    supported_python_versions="3.6.2",
    doc_service="rtd",
    doc_host_aws_profile_name="sanhe",
    doc_host_s3_bucket_name="sanherabbit.com",
    is_aws_lambda_project="Yes",
    lambda_aws_profile_name="sanhe",
    lambda_deployment_s3_bucket_name="sanhe-learn-aws-lambda-with-sls-deploy",
    lambda_layer_arn="",
    lambda_execution_role_arn="",
    use_pyenv="Y",

    _dev_py_ver_major=sys.version_info.major,
    _dev_py_ver_minor=sys.version_info.minor,
    _dev_py_ver_micro=sys.version_info.micro,
    _dev_py_ver_full="{}.{}.{}".format(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro,
    ),
    _current_year=datetime.now().year,
    _current_date=str(date.today()),
    _cookiecutter_pygitrepo_version=cookiecutter_pygitrepo_version,
)

def run_cookie_cutter():
    cookiecutter(
        here,
        extra_context=extra_context,
        no_input=True,
        overwrite_if_exists=True,
    )


if __name__ == "__main__":
    run_cookie_cutter()
