# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
from datetime import datetime, date
from cookiecutter.main import cookiecutter

here = os.path.dirname(__file__)

extra_context = dict(
    package_name="learn_cc",
    github_username="MacHu-GWU",
    author_name="Sanhe Hu",
    author_email="husanhe@gmail.com",
    command_line_interface="Click",
    supported_python_versions="2.7.13 3.6.2",
    doc_service="s3",
    doc_host_aws_profile_name="sanhe",
    doc_host_s3_bucket_name="sanherabbit.com",
    is_aws_project="Y",
    aws_profile_name="sanhe",
    deployment_s3_bucket_name="sanhe-admin-deployment",
    is_aws_lambda_project="Y",
    is_aws_cloudformation_project="Y",
    use_pyenv="N",

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
