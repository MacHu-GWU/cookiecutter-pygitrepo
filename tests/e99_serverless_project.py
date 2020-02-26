# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
from datetime import datetime, date
from cookiecutter.main import cookiecutter

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(PROJECT_ROOT, "version.txt"), "rb") as f:
    _cookiecutter_pygitrepo_version = f.read().decode("utf-8").strip()

aws_account_id = os.environ["AWS_ACCOUNT_ID"]

extra_context = dict(
    package_name="a_micro_service",
    package_name_slug="a-micro-service",
    repo_name="a_micro_service-project",
    github_username="My-GitHub-Username",
    author_name="My Author Name",
    author_email="author@example.com",
    has_command_line_interface="Y",
    supported_python_versions="3.6.2 3.7.2",
    use_pyenv="N",
    cicd_service="circleci",
    doc_service="s3",
    rtd_project_name="",
    doc_host_aws_profile_name="sanhe",
    doc_host_s3_bucket_name="sanherabbit.com",
    want_devops_tools="Y",
    is_aws_project="Y",
    aws_profile_name="sanhe",
    aws_region="us-east-1",
    aws_account_id=aws_account_id,
    deployment_s3_bucket_name="sanhe-admin-for-everything",
    is_aws_lambda_project="Y",
    is_aws_cloudformation_project="Y",
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
    _cookiecutter_pygitrepo_version=_cookiecutter_pygitrepo_version,
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
