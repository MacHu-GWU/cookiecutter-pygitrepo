#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import os
import sys
import shutil
from zipfile import ZipFile
from pygitrepo import pgr
from pygitrepo_print import Fore, Style


def rm_if_exists(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    else:
        return


def mkdir_if_not_exists(path):
    if os.path.exists(path):
        return
    else:
        os.makedirs(path)


ignore_dependencies = {
    "boto3",
    "botocore",
    "s3transfer",
    "setuptools",
    "pip",
    "wheel",
    "twine",
    "_pytest",
    "pytest",
}


class PyGitRepoFunc(object):
    def build_lbd_source(self):
        print(
            "[pygitrepo] "
            + Fore.CYAN
            + "build lambda source code at "
            + Style.RESET_ALL
            + pgr.PATH_LAMBDA_BUILD_SOURCE
        )

        dir_project_root = pgr.DIR_PROJECT_ROOT
        to_zip_list = list()
        for dirname, _, basename_list in os.walk(pgr.DIR_PYTHON_LIB):
            for basename in basename_list:
                if basename.endswith(".pyc") \
                    or basename.endswith(".pyo") \
                    or dirname.endswith("__pycache__"):
                    continue
                abspath = os.path.join(dirname, basename)
                arch_path = os.path.relpath(abspath, dir_project_root)
                to_zip_list.append((abspath, arch_path))

        print(
            "[pygitrepo] "
            + Fore.CYAN
            + "  zip "
            + Style.RESET_ALL
            + pgr.DIR_VENV_SITE_PACKAGES
        )

        mkdir_if_not_exists(pgr.DIR_LAMBDA_BUILD)
        rm_if_exists(pgr.PATH_LAMBDA_BUILD_SOURCE)
        with ZipFile(pgr.PATH_LAMBDA_BUILD_SOURCE, "w") as f:
            for abspath, arch_path in to_zip_list:
                f.write(abspath, arch_path)

        print("[pygitrepo] " + Fore.CYAN + "  done" + Style.RESET_ALL)

    def build_lbd_layer(self):
        print(
            "[pygitrepo] "
            + Fore.CYAN
            + "build lambda layer at "
            + Style.RESET_ALL
            + pgr.PATH_LAMBDA_BUILD_LAYER
        )

        dir_venv_site_packages = pgr.DIR_VENV_SITE_PACKAGES
        to_zip_list = list()
        ignore = {
            pgr.PACKAGE_NAME,
            "{}-{}.dist-info".format(pgr.PACKAGE_NAME, pgr.PACKAGE_VERSION)
        }.union(ignore_dependencies)
        for basename in os.listdir(dir_venv_site_packages):
            if basename in ignore or basename.split("-")[0] in ignore:
                continue
            abspath = os.path.join(dir_venv_site_packages, basename)
            if os.path.isfile(abspath):
                arch_path = os.path.join(
                    "python",
                    os.path.relpath(abspath, dir_venv_site_packages)
                )
                to_zip_list.append((abspath, arch_path))
            else:
                for dirname, _, basename_list in os.walk(
                    os.path.join(dir_venv_site_packages, basename)):
                    for basename in basename_list:
                        abspath = os.path.join(dirname, basename)
                        arch_path = os.path.join(
                            "python",
                            os.path.relpath(abspath, dir_venv_site_packages)
                        )
                        to_zip_list.append((abspath, arch_path))

        print(
            "[pygitrepo] "
            + Fore.CYAN
            + "  zip "
            + Style.RESET_ALL
            + pgr.DIR_VENV_SITE_PACKAGES
        )

        mkdir_if_not_exists(pgr.DIR_LAMBDA_BUILD)
        rm_if_exists(pgr.PATH_LAMBDA_BUILD_LAYER)
        with ZipFile(pgr.PATH_LAMBDA_BUILD_LAYER, "w") as f:
            for abspath, arch_path in to_zip_list:
                f.write(abspath, arch_path)

        print("[pygitrepo] " + Fore.CYAN + "  done" + Style.RESET_ALL)

    def build_lbd_deploy_package(self):
        print(
            "[pygitrepo] "
            + Fore.CYAN
            + "build lambda deploy package at "
            + Style.RESET_ALL
            + pgr.PATH_LAMBDA_BUILD_DEPLOY_PACKAGE
        )
        dir_venv_site_packages = pgr.DIR_VENV_SITE_PACKAGES
        to_zip_list = list()
        ignore = ignore_dependencies
        for basename in os.listdir(dir_venv_site_packages):
            if basename in ignore or basename.split("-")[0] in ignore:
                continue
            abspath = os.path.join(dir_venv_site_packages, basename)
            if os.path.isfile(abspath):
                arch_path = os.path.relpath(abspath, dir_venv_site_packages)
                to_zip_list.append((abspath, arch_path))
            else:
                for dirname, _, basename_list in os.walk(
                    os.path.join(dir_venv_site_packages, basename)):
                    for basename in basename_list:
                        abspath = os.path.join(dirname, basename)
                        arch_path = os.path.relpath(abspath, dir_venv_site_packages)
                        to_zip_list.append((abspath, arch_path))

        print(
            "[pygitrepo] "
            + Fore.CYAN
            + "  zip "
            + Style.RESET_ALL
            + pgr.DIR_VENV_SITE_PACKAGES
        )

        mkdir_if_not_exists(pgr.DIR_LAMBDA_BUILD)
        rm_if_exists(pgr.PATH_LAMBDA_BUILD_DEPLOY_PACKAGE)
        with ZipFile(pgr.PATH_LAMBDA_BUILD_DEPLOY_PACKAGE, "w") as f:
            for abspath, arch_path in to_zip_list:
                f.write(abspath, arch_path)

        print("[pygitrepo] " + Fore.CYAN + "  done" + Style.RESET_ALL)


pgr_func = PyGitRepoFunc()

if __name__ == "__main__":
    method_name = sys.argv[1]
    getattr(pgr_func, method_name)()

    # Test code
    # pgr_func.build_lbd_deploy_package()
