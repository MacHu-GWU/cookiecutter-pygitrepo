# -*- coding: utf-8 -*-

"""
This is a drop-in-ready script.
"""

import os
from os.path import (
    basename, join, abspath, dirname, exists, expanduser
)
import sys
import platform
from collections import OrderedDict


def ensure_list(value):
    if value is None:
        return []
    return value


class PyVer(object):
    def __init__(self, version):
        self.version = version

        try:
            self.validate_version(version)
        except:
            error = "'%s' is not a valid Python Version. It should be like ${major}.${minor}.{micro}. For example: '3.6.8'" % version
            raise ValueError(error)

        chunks = version.split(".")
        self.major = int(chunks[0])
        self.minor = int(chunks[1])
        self.micro = int(chunks[2])

    def validate_version(self, version):
        assert version.count(".") == 2
        chunks = version.split(".")
        major = int(chunks[0])
        minor = int(chunks[1])
        micro = int(chunks[2])
        assert major in [2, 3]

    @property
    def major_and_minor(self):
        return "{}.{}".format(self.major, self.minor)


class OS:
    windows = "Windows"
    darwin = "Darwin"
    linux = "Linux"
    java = "Java"


class Project(object):
    def __init__(self,
                 dir_project_root=None,
                 package_name=None,
                 pypi_name=None,
                 rtd_name=None,
                 python_version_for_dev=None,
                 python_versions_to_support=None,
                 aws_s3_bucket_for_deploy=None,
                 aws_s3_bucket_for_docs=None):
        self.dir_project_root = abspath(dir_project_root)  # type: str
        self.package_name = package_name  # type: str
        self.pypi_name = pypi_name  # type: str
        self.rtd_name = rtd_name  # type: str

        PyVer(python_version_for_dev) # validate
        self.python_version_for_dev = python_version_for_dev  # type: str

        _ = [ # validate
            PyVer(version)
            for version in ensure_list(python_versions_to_support)
        ]
        self.python_versions_to_support = python_versions_to_support  # type: list[str]
        self.aws_s3_bucket_for_deploy = aws_s3_bucket_for_deploy
        self.aws_s3_bucket_for_docs = aws_s3_bucket_for_docs

        self.home = abspath(expanduser("~"))
        self.post_init_detect_os()
        self.post_init_detect_runtime()

    def post_init_detect_os(self):
        self.os = platform.system()
        self.is_windows = self.os == OS.windows
        self.is_mac = self.os == OS.darwin
        self.is_linux = self.os == OS.linux
        self.is_java = self.os == OS.java

    def post_init_detect_runtime(self):
        self.is_ci_runtime = "CI" in os.environ
        self.is_jenkins_runtime = "JENKINS_HOME" in os.environ
        # ref: https://circleci.com/docs/2.0/env-vars/#built-in-environment-variables
        self.is_circleci_runtime = "CIRCLECI" in os.environ
        # ref: https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html
        self.is_aws_codebuild_runtime = "CODEBUILD_BUILD_ID" in os.environ
        # ref: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
        self.is_travis = "TRAVIS" in os.environ

        # AWS
        # ec2
        if self.is_windows:
            pass
        elif self.is_java:
            pass
        else:
            hypervisor_uuid_file = "/sys/hypervisor/uuid"
            if os.path.exists(hypervisor_uuid_file):
                with open(hypervisor_uuid_file, "rb") as f:
                    hypervisor_uuid = f.read().decode("utf-8").strip()
                self.is_aws_ec2_runtime = hypervisor_uuid.startswith("ec2")
            self.is_aws_ec2_runtime = False
        # lambda
        # ref: https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-config
        self.is_aws_lambda_runtime = "AWS_LAMBDA_FUNCTION_NAME" in os.environ
        # this is not supported by default, it is my personal best practice that
        # always set IS_AWS_ECS env var
        self.is_aws_ecs_runtime = "IS_AWS_ECS" in os.environ

    @property
    def git_repo_name(self):
        return basename(self.dir_project_root)

    @property
    def package_name_slugify(self):
        """
        :rtype: str
        """
        return self.package_name.replace("_", "-")

    @property
    def project_version(self):
        """
        Get the project version. It should be in the
        ``${dir_project_root}/${package_name}/_version.py`` file.

        The content should be::
        
            __version__ = "a.b.c"
        """
        path = join(self.dir_project_root, self.package_name)
        if path not in sys.path:
            sys.path.append(path)
        from _version import __version__
        return __version__

    def _if_none_then_package_name(self, value):
        if value is None:
            return self.package_name
        return value

    @property
    def python_package_index_name(self):
        """
        :rtype: str
        """
        return self._if_none_then_package_name(self.pypi_name)

    @property
    def read_the_doc_name(self):
        """
        :rtype: str
        """
        return self._if_none_then_package_name(self.read_the_doc_name)

    # === Repo file structure ===
    @property
    def path_readme(self):
        return join(self.dir_project_root, "README.rst")

    @property
    def dir_package_source(self):
        return join(self.dir_project_root, self.package_name)

    @property
    def path_package_version_file(self):
        return join(self.dir_package_source, "_version.py")

    @property
    def path_setup_script(self):
        return join(self.dir_project_root, "setup.py")

    @property
    def path_manifest_file(self):
        return join(self.dir_project_root, "MANIFEST.in")

    @property
    def path_license_file(self):
        return join(self.dir_project_root, "LICENSE.txt")

    @property
    def path_author_file(self):
        return join(self.dir_project_root, "AUTHORS.rst")

    @property
    def path_release_history_file(self):
        return join(self.dir_project_root, "release-history.rst")

    # required library, dependency file
    @property
    def path_requirements_file(self):
        return join(self.dir_project_root, "requirements.py")

    @property
    def path_requirements_dev_file(self):
        return join(self.dir_project_root, "requirements-dev.py")

    @property
    def path_requirements_doc_file(self):
        return join(self.dir_project_root, "requirements-doc.py")

    @property
    def path_requirements_test_file(self):
        return join(self.dir_project_root, "requirements-test.py")

    # pytest
    @property
    def dir_unittest(self):
        return join(self.dir_project_root, "tests")

    @property
    def dir_pytest_cache(self):
        return join(self.dir_project_root, ".pytest_cache")

    # code coverage test
    @property
    def path_coveragerc_file(self):
        """
        The code coverage configuration file for python code coverage library
        https://github.com/nedbat/coveragepy
        """
        return join(self.dir_project_root, ".coveragerc")

    @property
    def dir_coverage_annotate(self):
        """
        The code coverage result annotaton dir.
        https://github.com/nedbat/coveragepy
        """
        return join(self.dir_project_root, ".coverage.annotate")

    @property
    def path_codecov_yml_file(self):
        """
        The code coverage as service platform config yaml file
        https://about.codecov.io/
        """
        return join(self.dir_project_root, "codecov.yml")

    # matrix test
    @property
    def path_tox_ini_file(self):
        """
        The config file for multi python version and matrix testing tox framework.
        https://tox.readthedocs.io/en/latest/config.html?highlight=tox%20ini
        """
        return join(self.dir_project_root, "tox.ini")

    @property
    def dir_tox_workspace(self):
        """
        The tox workspace temp dir.
        """
        return join(self.dir_project_root, ".tox")

    @property
    def path_auto_pep8_script(self):
        """
        A python script that auto pep8 format all source code.
        """
        return join(self.dir_project_root, "fix_code_style.py")

    @property
    def dir_build(self):
        return join(self.dir_project_root, "build")

    @property
    def dir_dist(self):
        return join(self.dir_project_root, "dist")

    @property
    def dir_egg_info(self):
        return join(self.dir_project_root, "{}.egg-info".format(self.package_name))

    # === Documentation Option ===
    # sphinx-doc + readthe doc
    @property
    def dir_sphinx_doc(self):
        return join(self.dir_project_root, "docs")

    @property
    def dir_sphinx_source(self):
        return join(self.dir_sphinx_doc, "source")

    @property
    def dir_sphinx_build(self):
        return join(self.dir_sphinx_doc, "build")

    @property
    def dir_sphinx_build_html(self):
        return join(self.dir_sphinx_build, "html")

    @property
    def path_sphinx_build_html_index(self):
        return join(self.dir_sphinx_build, "index.html")

    @property
    def path_sphinx_config_file(self):
        return join(self.dir_sphinx_source, "conf.py")

    @property
    def path_readthedoc_yml_file(self):
        return join(self.dir_project_root, "readthedocs.yml")

    # AWS S3

    # --- Virtualenv related path
    @property
    def venv_name(self):
        return "{}_venv".format(self.package_name)

    @property
    def dir_venv(self):
        return join(
            self.home,
            "venvs",
            "python",
            PyVer(self.python_version_for_dev).major_and_minor,
            self.venv_name,
        )

    @property
    def dir_venv_bin(self):
        if self.is_windows:
            return join(self.dir_venv, "Scripts")
        else:
            return join(self.dir_venv, "bin")

    @property
    def dir_venv_site_packages(self):
        if self.is_windows:
            return join(self.dir_venv, "Lib", "site-packages")
        else:
            return join(self.dir_venv, "lib", PyVer(self.python_version_for_dev).major_and_minor, "site-packages")

    @property
    def dir_venv_site_packages64(self):
        if self.is_windows:
            return join(self.dir_venv, "Lib64", "site-packages")
        else:
            return join(self.dir_venv, "lib64", PyVer(self.python_version_for_dev).major_and_minor, "site-packages")

    @property
    def bin_venv_activate(self):
        return join(self.dir_venv_bin, "activate")

    @property
    def bin_venv_python(self):
        return join(self.dir_venv_bin, "python")

    @property
    def bin_venv_pip(self):
        return join(self.dir_venv_bin, "pip")

    @property
    def bin_venv_pytest(self):
        return join(self.dir_venv_bin, "pytest")

    @property
    def bin_venv_twine(self):
        return join(self.dir_venv_bin, "twine")

    @property
    def bin_venv_tox(self):
        return join(self.dir_venv_bin, "tox")

    @property
    def bin_venv_jupyter(self):
        return join(self.dir_venv_bin, "jupyter")

    @property
    def bin_venv_sphinx_quick_start(self):
        return join(self.dir_venv_bin, "sphinx-quickstart")

    @property
    def bin_venv_aws(self):
        return join(self.dir_venv_bin, "aws")

    @property
    def bin_venv_ansible(self):
        return join(self.dir_venv_bin, "ansible")

    # === CI Option ===

    # --- GitHub Action ---
    @property
    def path_github_action_main_workflow_file(self):
        return join(self.dir_project_root, ".github", "workflows", "main.yml")

    # === AWS Lambda Function ===
    @property
    def dir_lbd_build(self):
        return join(self.dir_build, "lambda")

    @property
    def dir_lbd_site_packages(self):
        return join(self.dir_lbd_build, "site-packages")

    @property
    def path_lbd_source_file(self):
        """
        Lambda function source code only. Dependencies not included.
        """
        return join(self.dir_lbd_build, "source.zip")

    @property
    def path_lbd_layer_file(self):
        """
        Lambda function dependencies only. Usually for Lambda Layer.
        """
        return join(self.dir_lbd_build, "layer.zip")

    @property
    def path_lbd_deploy_pkg_file(self):
        """
        Lambda function source code and dependencies in the same site-packages
        directory.
        """
        return join(self.dir_lbd_build, "deploy-pkg.zip")

    @property
    def s3_prefix_lambda_deploy_repo_root(self):
        return "lambda/deploy/{}".format(self.git_repo_name)

    @property
    def aws_console_url_s3_lambda_deploy(self):
        """
        """
        return "https://s3.console.aws.amazon.com/s3/buckets/{}?prefix={}/".format(
            self.aws_s3_bucket_for_deploy,
            self.s3_prefix_lambda_deploy_repo_root,
        )

    @property
    def s3_key_lambda_source_file(self):
        return "{}/{}/source.zip".format(
            self.s3_prefix_lambda_deploy_repo_root,
            self.project_version,
        )

    @property
    def s3_key_lambda_layer_file(self):
        return "{}/{}/layer.zip".format(
            self.s3_prefix_lambda_deploy_repo_root,
            self.project_version,
        )

    @property
    def s3_key_lambda_deploy_pkg_file(self):
        return "{}/{}/deploy-pkg.zip".format(
            self.s3_prefix_lambda_deploy_repo_root,
            self.project_version,
        )

    @property
    def s3_uri_lambda_source_file(self):
        return "s3://{}/{}".format(self.aws_s3_bucket_for_deploy, self.s3_key_lambda_source_file)

    @property
    def s3_uri_lambda_layer_file(self):
        return "s3://{}/{}".format(self.aws_s3_bucket_for_deploy, self.s3_key_lambda_layer_file)

    @property
    def s3_uri_lambda_deploy_pkg_file(self):
        return "s3://{}/{}".format(self.aws_s3_bucket_for_deploy, self.s3_key_lambda_deploy_pkg_file)


def get_attr(args, project):
    """
    Print an attribute of the Project object for shell script to use.
    """
    value = getattr(project, args.attr_name)
    print(value)


def list_attr(args, project):
    """
    List available valid attributes of the Project object.
    """
    # collect valid Project attributes
    valid_attrs = OrderedDict()

    for key in project.__dict__:
        if not key.startswith("_"):
            valid_attrs[key] = 0

    for key, value in Project.__dict__.items():
        if isinstance(value, property) and (not key.startswith("_")):
            valid_attrs[key] = 0

    # list attributes
    if args.filter:
        for attr_name in valid_attrs:
            if args.filter in attr_name:
                print(attr_name)
    else:
        for attr_name in valid_attrs:
            print(attr_name)


class SubCommand:
    get_attr = "get-attr"
    list_attr = "list-attr"


sub_command_callers = {
    SubCommand.get_attr: get_attr,
    SubCommand.list_attr: list_attr,
}


def main(args, project):
    return sub_command_callers[args.sub_command](args, project)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers(
        title="sub commands",
        help="sub-command help"
    )

    # subcommand get-attr
    parser_get_attr = subparsers.add_parser(
        SubCommand.get_attr,
        help="get value of an attribute of Project object."
    )
    parser_get_attr.add_argument(
        "attr_name",
        type=str,
        help="The attribute name of the Project object."
    )
    parser_get_attr.set_defaults(sub_command=SubCommand.get_attr)

    # subcommand list-attr
    parser_list_attr = subparsers.add_parser(
        SubCommand.list_attr,
        help="list valid attribute of Project object."
    )

    parser_list_attr.add_argument(
        "--filter",
        type=str,
        dest="filter",
        required=False,
    )
    parser_list_attr.set_defaults(sub_command=SubCommand.list_attr)

    #--- parse cli argument
    args = parser.parse_args()

    #--- prepare Project object
    dir_project_root = dirname(abspath(__file__))

    dir_project_root = join(dirname(dir_project_root), "cottonformation-project")
    package_name = "cottonformation"
    # package_name = "hello_world"
    python_version_for_dev = "3.6.2"
    python_versions_to_support = ["3.6.2", "3.7.9"]

    project = Project(
        dir_project_root=dir_project_root,
        package_name=package_name,
        python_version_for_dev=python_version_for_dev,
        python_versions_to_support=python_versions_to_support,
    )

    # main(args, project)

    print(project.project_version)