#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Print useful information related to this python git repository.

Usage::

.. code-block:: bash

    $ python pygitrepo_info.py
"""

from __future__ import print_function, unicode_literals
from os.path import exists
from pygitrepo_print import Fore, Style
from pygitrepo_config import Config
from pygitrepo import pgr

print("[pygitrepo] {COLOR}print useful information:{RESET}".format(
    COLOR=Fore.CYAN,
    RESET=Style.RESET_ALL,
))

print("------ Paths: {RED}red = not exists, {GREEN} green = exists {RESET}------".format(
    RED=Fore.RED,
    GREEN=Fore.GREEN,
    RESET=Style.RESET_ALL,
))
print("- virtualenv at: {COLOR}{path}{RESET}".format(
    COLOR=Fore.GREEN if exists(pgr.DIR_VENV) else Fore.RED,
    path=pgr.DIR_VENV,
    RESET=Style.RESET_ALL,
))
print("- venv python at: {COLOR}{path}{RESET}".format(
    COLOR=Fore.GREEN if exists(pgr.PATH_VENV_BIN_PYTHON) else Fore.RED,
    path=pgr.PATH_VENV_BIN_PYTHON,
    RESET=Style.RESET_ALL,
))
print("- venv pip at: {COLOR}{path}{RESET}".format(
    COLOR=Fore.GREEN if exists(pgr.PATH_VENV_BIN_PIP) else Fore.RED,
    path=pgr.PATH_VENV_BIN_PIP,
    RESET=Style.RESET_ALL,
))
print("- activate venv: source {COLOR}{path}{RESET}".format(
    COLOR=Fore.GREEN if exists(pgr.PATH_VENV_BIN_ACTIVATE) else Fore.RED,
    path=pgr.PATH_VENV_BIN_ACTIVATE,
    RESET=Style.RESET_ALL,
))
print("- deactivate venv: deactivate")
print("- site-packages at: {COLOR}{path}{RESET}".format(
    COLOR=Fore.GREEN if exists(pgr.DIR_VENV_SITE_PACKAGES) else Fore.RED,
    path=pgr.DIR_VENV_SITE_PACKAGES,
    RESET=Style.RESET_ALL,
))
print("- {package_name} installed at: {COLOR1}{path1}{RESET} or {COLOR2}{path2}{RESET}".format(
    package_name=Config.PACKAGE_NAME,
    COLOR1=Fore.GREEN if exists(pgr.DIR_VENV_SITE_PACKAGES_INSTALLED) else Fore.RED,
    path1=pgr.DIR_VENV_SITE_PACKAGES_INSTALLED,
    COLOR2=Fore.GREEN if exists(pgr.DIR_VENV_SITE_PACKAGES_EGG_LINK) else Fore.RED,
    path2=pgr.DIR_VENV_SITE_PACKAGES_EGG_LINK,
    RESET=Style.RESET_ALL,
))
print("- local html doc at: {COLOR}{path}{RESET}".format(
    COLOR=Fore.GREEN if exists(pgr.PATH_SPHINX_DOC_BUILD_HTML_INDEX) else Fore.RED,
    path=pgr.PATH_SPHINX_DOC_BUILD_HTML_INDEX,
    RESET=Style.RESET_ALL,
))

print("------ Urls: ------{RESET}".format(
    RESET=Style.RESET_ALL,
))
print("- latest doc on readthedocs: {}".format(pgr.URL_RTD_DOC))
print("- latest doc on AWS S3: {}".format(pgr.URL_S3_DOC_LATEST))
print("- versioned doc on AWS S3: {}".format(pgr.URL_S3_DOC_VERSIONED))
