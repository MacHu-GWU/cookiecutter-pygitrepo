#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find a named value.

Usage:

.. code-block:: bash

    # syntax
    $ named_value="$(python pygitrepo.py ${property_name})"

    # example
    $ python pygitrepo.py DIR_PROJECT_ROOT
"""

from __future__ import unicode_literals
import sys
from os.path import (
    abspath, dirname, basename, expanduser, join, exists
)
from pygitrepo_config import Config
from pygitrepo_os import (
    OS_NAME, OSEnum,
    IS_WINDOWS, IS_MACOS, IS_LINUX, IS_JAVA,
    OPEN_COMMAND,
)

PYGITREPO_UNKNOWN = "[pygitrepo] Unknown"


def make_s3_console_url(bucket, prefix):
    if prefix.endswith("/"):
        s3_type = "buckets"
    else:
        s3_type = "object"
    return "https://s3.console.aws.amazon.com/s3/{s3_type}/{bucket}?prefix={prefix}".format(
        s3_type=s3_type,
        bucket=bucket,
        prefix=prefix
    )


def s3_key_join(parts, is_dir):
    new_parts = list()
    for part in parts:
        new_parts.extend([chunk for chunk in part.split("/") if chunk])
    key = "/".join(new_parts)
    if is_dir:
        return key + "/"
    else:
        return key


class PyGitRepo(object):
    def __init__(self):
        self.DIR_HERE = dirname(abspath(__file__))
        self.DIR_HOME = expanduser("~")

        self.GITHUB_ACCOUNT = Config.GITHUB_ACCOUNT
        self.GITHUB_REPO_NAME = Config.GITHUB_REPO_NAME
        self.PACKAGE_NAME = Config.PACKAGE_NAME
        self.PACKAGE_NAME_SLUGIFY = Config.PACKAGE_NAME.replace("_", "-")
        self.DEV_PY_VER_MAJOR = Config.DEV_PY_VER_MAJOR
        self.DEV_PY_VER_MINOR = Config.DEV_PY_VER_MINOR
        self.DEV_PY_VER_MICRO = Config.DEV_PY_VER_MICRO
        self.TOX_TEST_VERSIONS = Config.TOX_TEST_VERSIONS

        self.DOC_HOST_RTD_PROJECT_NAME = Config.DOC_HOST_RTD_PROJECT_NAME
        self.DOC_HOST_AWS_PROFILE = Config.DOC_HOST_AWS_PROFILE
        self.DOC_HOST_S3_BUCKET = Config.DOC_HOST_S3_BUCKET

        # --- AWS Lambda Related
        self.AWS_LAMBDA_DEPLOY_AWS_PROFILE = Config.AWS_LAMBDA_DEPLOY_AWS_PROFILE
        self.AWS_LAMBDA_DEPLOY_S3_BUCKET = Config.AWS_LAMBDA_DEPLOY_S3_BUCKET
        self.AWS_LAMBDA_BUILD_DOCKER_IMAGE = Config.AWS_LAMBDA_BUILD_DOCKER_IMAGE
        self.AWS_LAMBDA_BUILD_DOCKER_IMAGE_WORKSPACE_DIR = Config.AWS_LAMBDA_BUILD_DOCKER_IMAGE_WORKSPACE_DIR
        self.AWS_LAMBDA_TEST_DOCKER_IMAGE = Config.AWS_LAMBDA_TEST_DOCKER_IMAGE

        self.OS_NAME = OS_NAME
        self.IS_WINDOWS = IS_WINDOWS
        self.IS_MACOS = IS_MACOS
        self.IS_LINUX = IS_LINUX
        self.IS_JAVA = IS_JAVA
        self.OPEN_COMMAND = OPEN_COMMAND

    # === Code File Structure
    @property
    def DIR_BIN(self):
        return dirname(self.DIR_HERE)

    @property
    def DIR_BIN_PGR(self):
        return self.DIR_HERE

    @property
    def DIR_BIN_PY(self):
        return join(self.DIR_HERE, "py")

    @property
    def DIR_BIN_LBD(self):
        return join(self.DIR_HERE, "lbd")

    @property
    def DIR_PROJECT_ROOT(self):
        return dirname(dirname(self.DIR_HERE))

    # --- python project basics
    @property
    def PATH_README(self):
        return join(self.DIR_PROJECT_ROOT, "README.rst")

    @property
    def DIR_PYTHON_LIB(self):
        return join(self.DIR_PROJECT_ROOT, self.PACKAGE_NAME)

    @property
    def PATH_VERSION_FILE(self):
        return join(self.DIR_PYTHON_LIB, "_version.py")

    @property
    def PACKAGE_VERSION(self):
        sys.path.append(self.DIR_PYTHON_LIB)
        try:
            from _version import __version__
            return __version__
        except:
            return PYGITREPO_UNKNOWN

    @property
    def PATH_REQUIREMENTS_FILE(self):
        return join(self.DIR_PROJECT_ROOT, "requirements.txt")

    @property
    def PATH_REQUIREMENTS_DEV_FILE(self):
        return join(self.DIR_PROJECT_ROOT, "requirements-dev.txt")

    @property
    def PATH_REQUIREMENTS_DOC_FILE(self):
        return join(self.DIR_PROJECT_ROOT, "requirements-doc.txt")

    @property
    def PATH_REQUIREMENTS_TEST_FILE(self):
        return join(self.DIR_PROJECT_ROOT, "requirements-test.txt")

    @property
    def DIR_PYPI_BUILD(self):
        return join(self.DIR_PROJECT_ROOT, "build")

    @property
    def DIR_PYPI_DISTRIBUTE(self):
        return join(self.DIR_PROJECT_ROOT, "dist")

    @property
    def DIR_PYPI_EGG(self):
        return join(self.DIR_PROJECT_ROOT, "{}.egg-info".format(Config.PACKAGE_NAME))

    # --- testing
    @property
    def DIR_TESTS(self):
        return join(self.DIR_PROJECT_ROOT, "tests")

    @property
    def DIR_UNIT_TESTS(self):
        return self.DIR_TESTS

    @property
    def DIR_INTEGRATION_TESTS(self):
        return join(self.DIR_PROJECT_ROOT, "tests_integration")

    @property
    def DIR_PYTEST_CACHE(self):
        return join(self.DIR_PROJECT_ROOT, ".pytest_cache")

    @property
    def PATH_CODECOV_YML(self):
        return join(self.DIR_PROJECT_ROOT, "codecov.yml")

    @property
    def PATH_COVERAGE_CONFIG(self):
        return join(self.DIR_PROJECT_ROOT, ".coveragerc")

    @property
    def DIR_COVERAGE_ANNOTATE(self):
        return join(self.DIR_PROJECT_ROOT, ".coverage.annotate")

    @property
    def PYENV_LOCAL_VERSIONS_FOR_TOX(self):
        try:
            return " ".join(self.TOX_TEST_VERSIONS)
        except:
            return PYGITREPO_UNKNOWN

    # --- sphinx doc
    @property
    def DIR_SPHINX_DOC(self):
        return join(self.DIR_PROJECT_ROOT, "docs")

    @property
    def DIR_SPHINX_DOC_SOURCE(self):
        return join(self.DIR_SPHINX_DOC, "source")

    @property
    def DIR_SPHINX_DOC_SOURCE_CONFIG(self):
        return join(self.DIR_SPHINX_DOC_SOURCE, "conf.py")

    @property
    def DIR_SPHINX_DOC_BUILD(self):
        return join(self.DIR_SPHINX_DOC, "build")

    @property
    def DIR_SPHINX_DOC_BUILD_HTML(self):
        return join(self.DIR_SPHINX_DOC_BUILD, "html")

    @property
    def PATH_SPHINX_DOC_BUILD_HTML_INDEX(self):
        return join(self.DIR_SPHINX_DOC_BUILD_HTML, "index.html")

    @property
    def PATH_READTHEDOCS_YML(self):
        return join(self.DIR_PROJECT_ROOT, "readthedocs.yml")

    @property
    def URL_RTD_DOC(self):
        return "https://{}.readthedocs.io/".format(Config.DOC_HOST_RTD_PROJECT_NAME)

    @property
    def URL_S3_DOC_LATEST(self):
        return "https://{bucket}.s3.amazonaws.com/docs/{package_name}/latest/".format(
            bucket=self.DOC_HOST_S3_BUCKET,
            package_name=self.PACKAGE_NAME,
        )

    @property
    def URL_S3_DOC_VERSIONED(self):
        return "https://{bucket}.s3.amazonaws.com/docs/{package_name}/{version}/index.html".format(
            bucket=self.DOC_HOST_S3_BUCKET,
            package_name=self.PACKAGE_NAME,
            version=self.PACKAGE_VERSION,
        )

    @property
    def S3_URI_DOC_DIR_LATEST(self):
        return "s3://{bucket}/docs/{package_name}/latest".format(
            bucket=self.DOC_HOST_S3_BUCKET,
            package_name=self.PACKAGE_NAME,
        )

    @property
    def S3_URI_DOC_DIR_VERSIONED(self):
        return "s3://{bucket}/docs/{package_name}/{version}".format(
            bucket=self.DOC_HOST_S3_BUCKET,
            package_name=self.PACKAGE_NAME,
            version=self.PACKAGE_VERSION,
        )

    @property
    def URL_S3_CONSOLE_LATEST_DOC_DIR(self):
        return make_s3_console_url(
            bucket=self.DOC_HOST_S3_BUCKET,
            prefix=s3_key_join(
                parts=[
                    "docs", self.PACKAGE_NAME, "latest"
                ],
                is_dir=True,
            )
        )

    @property
    def URL_S3_CONSOLE_VERSIONED_DOC_DIR(self):
        return make_s3_console_url(
            bucket=self.DOC_HOST_S3_BUCKET,
            prefix=s3_key_join(
                parts=[
                    "docs", self.PACKAGE_NAME, self.PACKAGE_VERSION
                ],
                is_dir=True,
            )
        )

    # === Pyenv
    @property
    def PATH_BIN_GLOBAL_PYTHON(self):
        if OS_NAME == OSEnum.windows:
            return "/c/Python{}.{}/python.exe".format(self.DEV_PY_VER_MAJOR, self.DEV_PY_VER_MINOR)
        elif OS_NAME in (OSEnum.macOS, OSEnum.linux):
            return join(
                self.DIR_HOME,
                ".pyenv",
                "shims",
                "python{}.{}".format(
                    self.DEV_PY_VER_MAJOR,
                    self.DEV_PY_VER_MINOR,
                )
            )
        else:
            raise EnvironmentError

    # === Virtualenv
    @property
    def VENV_NAME(self):
        return "{}_venv".format(Config.PACKAGE_NAME)

    @property
    def DIR_ALL_PYTHON_VERSIONED_VENV(self):
        if OS_NAME in (OSEnum.windows, OSEnum.macOS, OSEnum.linux):
            return join(
                self.DIR_HOME,
                "venvs",
                "python",
                "{}.{}.{}".format(
                    self.DEV_PY_VER_MAJOR,
                    self.DEV_PY_VER_MINOR,
                    self.DEV_PY_VER_MICRO,
                ),
            )
        else:
            raise ValueError

    @property
    def DIR_VENV(self):
        return join(self.DIR_ALL_PYTHON_VERSIONED_VENV, self.VENV_NAME)

    @property
    def DIR_VENV_SITE_PACKAGES(self):
        if OS_NAME == OSEnum.windows:
            return join(self.DIR_VENV, "Lib", "site-packages")
        elif OS_NAME in (OSEnum.macOS, OSEnum.linux):
            return join(
                self.DIR_VENV,
                "lib",
                "python{}.{}".format(Config.DEV_PY_VER_MAJOR, Config.DEV_PY_VER_MINOR),
                "site-packages",
            )
        else:
            raise Exception

    @property
    def DIR_VENV_SITE_PACKAGES_64(self):
        if OS_NAME == OSEnum.windows:
            return join(self.DIR_VENV, "Lib64", "site-packages")
        elif OS_NAME in (OSEnum.macOS, OSEnum.linux):
            return join(
                self.DIR_VENV,
                "lib64",
                "python{}.{}".format(Config.DEV_PY_VER_MAJOR, Config.DEV_PY_VER_MINOR),
                "site-packages",
            )
        else:
            raise Exception

    @property
    def DIR_VENV_SITE_PACKAGES_INSTALLED(self):
        return join(self.DIR_VENV_SITE_PACKAGES, Config.PACKAGE_NAME)

    @property
    def DIR_VENV_SITE_PACKAGES_EGG_LINK(self):
        return join(self.DIR_VENV_SITE_PACKAGES, "{}.egg-link".format(Config.PACKAGE_NAME).replace("_", "-"))

    # --- venv/bin
    @property
    def DIR_VENV_BIN(self):
        if OS_NAME == OSEnum.windows:
            return join(self.DIR_VENV, "Scripts")
        elif OS_NAME in (OSEnum.macOS, OSEnum.linux):
            return join(self.DIR_VENV, "bin")
        else:
            raise Exception

    @property
    def PATH_VENV_BIN_PYTHON(self):
        return join(self.DIR_VENV_BIN, "python")

    @property
    def PATH_VENV_BIN_ACTIVATE(self):
        return join(self.DIR_VENV_BIN, "activate")

    @property
    def PATH_VENV_BIN_PIP(self):
        return join(self.DIR_VENV_BIN, "pip")

    @property
    def PATH_VENV_BIN_PYTEST(self):
        return join(self.DIR_VENV_BIN, "pytest")

    @property
    def PATH_VENV_BIN_SPHINX_QUICKSTART(self):
        return join(self.DIR_VENV_BIN, "sphinx-quickstart")

    @property
    def PATH_VENV_BIN_TWINE(self):
        return join(self.DIR_VENV_BIN, "twine")

    @property
    def PATH_VENV_BIN_TOX(self):
        return join(self.DIR_VENV_BIN, "tox")

    @property
    def PATH_VENV_BIN_JUPYTER(self):
        return join(self.DIR_VENV_BIN, "jupyter")

    @property
    def PATH_VENV_BIN_ANSIBLE(self):
        return join(self.DIR_VENV_BIN, "ansible")

    @property
    def PATH_VENV_BIN_AWS(self):
        return join(self.DIR_VENV_BIN, "aws")

    @property
    def PATH_VENV_BIN_AWS_CHALICE(self):
        return join(self.DIR_VENV_BIN, "chalice")

    @property
    def PATH_VENV_BIN_AWS_ELASTIC_BEANSTALK(self):
        return join(self.DIR_VENV_BIN, "flask")

    # === AWS CLI
    @property
    def AWS_CLI_PROFILE_ARG_DOC_HOST(self):
        if Config.DOC_HOST_AWS_PROFILE:
            return Config.DOC_HOST_AWS_PROFILE
        else:
            return ""

    @property
    def AWS_CLI_PROFILE_ARG_LAMBDA_DEPLOY(self):
        if Config.AWS_LAMBDA_DEPLOY_AWS_PROFILE:
            return Config.AWS_LAMBDA_DEPLOY_AWS_PROFILE
        else:
            return ""

    # === AWS Lambda
    @property
    def DIR_LAMBDA_BUILD(self):
        return join(self.DIR_PYPI_BUILD, "lambda")

    @property
    def DIR_LAMBDA_BUILD_SITE_PACKAGES(self):
        return join(self.DIR_LAMBDA_BUILD, "site-packages")

    @property
    def PATH_LAMBDA_BUILD_DEPLOY_PACKAGE(self):
        return join(self.DIR_LAMBDA_BUILD, "deploy-pkg.zip")

    @property
    def PATH_LAMBDA_BUILD_SOURCE(self):
        return join(self.DIR_LAMBDA_BUILD, "source.zip")

    @property
    def PATH_LAMBDA_BUILD_LAYER(self):
        return join(self.DIR_LAMBDA_BUILD, "layer.zip")

    @property
    def S3_KEY_LAMBDA_DEPLOY_DIR(self):
        return s3_key_join(
            parts=[
                "lambda",
                self.PACKAGE_NAME,
            ],
            is_dir=True,
        )

    @property
    def S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR(self):
        return s3_key_join(
            parts=[
                self.S3_KEY_LAMBDA_DEPLOY_DIR,
                self.PACKAGE_VERSION,
            ],
            is_dir=True,
        )

    @property
    def S3_URI_LAMBDA_DEPLOY_VERSIONED_DIR(self):
        return "s3://{bucket}/{key}".format(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            key=self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR,
        )

    @property
    def S3_KEY_LAMBDA_DEPLOY_VERSIONED_SOURCE_DIR(self):
        return s3_key_join(
            parts=[
                self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR,
                "source",
            ],
            is_dir=True,
        )

    @property
    def S3_URI_LAMBDA_DEPLOY_VERSIONED_SOURCE_DIR(self):
        return "s3://{bucket}/{key}".format(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            key=self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_SOURCE_DIR,
        )

    @property
    def S3_KEY_LAMBDA_DEPLOY_VERSIONED_LAYER_DIR(self):
        return s3_key_join(
            parts=[
                self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR,
                "layer",
            ],
            is_dir=True,
        )

    @property
    def S3_URI_LAMBDA_DEPLOY_VERSIONED_LAYER_DIR(self):
        return "s3://{bucket}/{key}".format(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            key=self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_LAYER_DIR,
        )

    @property
    def S3_KEY_LAMBDA_DEPLOY_VERSIONED_DEPLOY_PKG_DIR(self):
        return s3_key_join(
            parts=[
                self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR,
                "deploy-pkg",
            ],
            is_dir=True,
        )

    @property
    def S3_URI_LAMBDA_DEPLOY_VERSIONED_DEPLOY_PKG_DIR(self):
        return "s3://{bucket}/{key}".format(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            key=self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DEPLOY_PKG_DIR,
        )

    @property
    def URL_S3_CONSOLE_LAMBDA_DEPLOY_DIR(self):
        return make_s3_console_url(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            prefix=self.S3_KEY_LAMBDA_DEPLOY_DIR,
        )

    @property
    def URL_S3_CONSOLE_LAMBDA_DEPLOY_VERSIONED_DIR(self):
        return make_s3_console_url(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            prefix=self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR,
        )

    @property
    def URL_S3_CONSOLE_LAMBDA_DEPLOY_VERSIONED_SOURCE_OBJ(self):
        return make_s3_console_url(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            prefix=s3_key_join(
                parts=[
                    self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR,
                    "source",
                ],
                is_dir=False,
            ),
        )

    @property
    def URL_S3_CONSOLE_LAMBDA_DEPLOY_VERSIONED_LAYER_OBJ(self):
        return make_s3_console_url(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            prefix=s3_key_join(
                parts=[
                    self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR,
                    "layer",
                ],
                is_dir=False,
            ),
        )

    @property
    def URL_S3_CONSOLE_LAMBDA_DEPLOY_VERSIONED_DEPLOY_PKG_OBJ(self):
        return make_s3_console_url(
            bucket=self.AWS_LAMBDA_DEPLOY_S3_BUCKET,
            prefix=s3_key_join(
                parts=[
                    self.S3_KEY_LAMBDA_DEPLOY_VERSIONED_DIR,
                    "deploy-pkg",
                ],
                is_dir=False,
            ),
        )

    @property
    def URL_LBD_LAYER_CONSOLE(self):
        return "https://console.aws.amazon.com/lambda/home?#/layers/{layer_name}".format(
            layer_name=self.PACKAGE_NAME
        )


pgr = PyGitRepo()

if __name__ == "__main__":
    attr_name = sys.argv[1]
    print(getattr(pgr, attr_name))
