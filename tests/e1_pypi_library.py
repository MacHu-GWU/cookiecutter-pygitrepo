# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
from datetime import datetime, date
from cookiecutter.main import cookiecutter

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

extra_context = dict(
    package_name="a_pypi_library",
    github_username="MacHu-GWU",
    author_name="Sanhe Hu",
    author_email="husanhe@gmail.com",
    command_line_interface="Click",
    supported_python_versions="3.6.2",
    doc_service="s3",
    doc_host_aws_profile_name="sanhe",
    doc_host_s3_bucket_name="sanherabbit.com",
    is_aws_project="N",
    aws_profile_name="sanhe",
    deployment_s3_bucket_name="sanhe-admin-deployment",
    is_aws_lambda_project="N",
    is_aws_cloudformation_project="N",
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
        PROJECT_ROOT,
        extra_context=extra_context,
        no_input=True,
        overwrite_if_exists=True,
    )


if __name__ == "__main__":
    run_cookie_cutter()
