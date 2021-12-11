# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
from datetime import date

import attr
from ._version import __version__


@attr.s
class Config(object):
    """
    1. Constant config values: from ``cookiecutter-pygitrepo.json`` file
    2. Derivable config values: from method that wrapped by @property
    3. Cookiecutter context: #1 + #2
    """
    package_name = attr.ib()  # type: str
    github_username = attr.ib()  # type: str
    repo_name = attr.ib()  # type: str
    author_name = attr.ib()  # type: str
    author_email = attr.ib()  # type: str
    has_command_line_interface = attr.ib()  # type: bool
    supported_python_versions = attr.ib()  # type: list[str]
    cicd_service = attr.ib()  # type: str

    doc_service = attr.ib()  # type: str
    rtd_project_name = attr.ib()  # type: str
    doc_host_aws_profile_name = attr.ib()  # type: str
    doc_host_s3_bucket_name = attr.ib()  # type: str

    is_aws_chalice_project = attr.ib()  # type: bool
    aws_lambda_deploy_aws_profile = attr.ib()  # type: str
    aws_lambda_deploy_s3_bucket_name = attr.ib()  # type: str

    is_aws_cottonformation_project = attr.ib()  # type: bool
    aws_cloudformation_deploy_aws_profile = attr.ib()  # type: str

    path_cookiecutter_pygitrepo_json = attr.ib(default=None)  # type: str

    class CICDServiceEnum:
        github = "github"
        circleci = "circleci"

    class DocServiceEnum:
        readthedocs = "rtd"
        s3 = "s3"

    @property
    def package_name_slug(self):
        return self.package_name.replace("_", "-")

    @cicd_service.validator
    def check_cicd_service(self, attribute, value):
        valid_cicd_service = [
            self.CICDServiceEnum.github,
            self.CICDServiceEnum.circleci,
        ]
        if value not in valid_cicd_service:
            raise ValueError("cicd_service has to be one of '{}'".format(
                str(valid_cicd_service)))

    @doc_service.validator
    def check_doc_service(self, attribute, value):
        valid_doc_service = [
            self.DocServiceEnum.readthedocs,
            self.DocServiceEnum.s3,
        ]
        if value not in valid_doc_service:
            raise ValueError("doc_service has to be one of '{}'".format(
                str(valid_doc_service)))

    @property
    def dev_py_ver_major(self):
        return sys.version_info.major

    @property
    def dev_py_ver_minor(self):
        return sys.version_info.minor

    @property
    def dev_py_ver_micro(self):
        return sys.version_info.micro

    @property
    def dev_py_ver_full(self):
        return "{}.{}.{}".format(
            self.dev_py_ver_major,
            self.dev_py_ver_minor,
            self.dev_py_ver_micro,
        )

    @property
    def current_year(self):
        return date.today().year

    @property
    def current_date(self):
        return str(date.today())

    @property
    def aws_lambda_build_docker_image(self):
        return "lambci/lambda:build-python{}.{}".format(
            self.dev_py_ver_major,
            self.dev_py_ver_minor,
        )

    @property
    def aws_lambda_build_docker_image_workspace_dir(self):
        return "/var/task"

    @property
    def cookiecutter_pygitrepo_version(self):
        return __version__

    def to_context_data(self):
        """
        :rtype: dict
        """
        # get constant values
        context_data = attr.asdict(self)
        # get derivable values
        for method_name, method in Config.__dict__.items():
            if isinstance(method, property):
                context_data[method_name] = getattr(self, method_name)
        return context_data
