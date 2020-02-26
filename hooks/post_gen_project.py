# -*- coding: utf-8 -*-

import os
import shutil

REPO_DIR = os.path.realpath(os.path.curdir)


def remove_file_or_dir(*parts):
    """

    :param parts: relpath of repository directory.
    """
    abspath = os.path.join(REPO_DIR, *parts)
    if os.path.isfile(abspath):
        os.remove(abspath)
    elif os.path.isdir(abspath):
        shutil.rmtree(abspath)

help_msg = \
"""
Things to do Next after generated the project skeleton:

    1. Update ``<repo_name>/AUTHORS.rst``
    2. Update ``<repo_name>/LICENSE.txt`` and ``__license__`` variable in 
        ``<repo_name>/<package_name>/__init__.py`` (Since we use MIT by default). 
        If you don't know how to choose an open source license, 
        read this https://choosealicense.com/ .
    3. I recommend to use pyenv (https://github.com/pyenv/pyenv) 
        for python development on MacOS. If you also like pyenv, 
        set ``USE_PYENV="Y"`` in ``<repo_name>/bin/setting.sh``
    4. Edit aws lambda specific setting in:
        - ./bin/settings.sh : lambda deployment s3 bucket and aws profile
        - ./serverless.yml : lambda execution role and layer ARN
"""


if __name__ == '__main__':
    if "{{ cookiecutter.has_command_line_interface }}" != "Y":
        remove_file_or_dir("{{ cookiecutter.package_name }}", "cli.py")

    if "{{ cookiecutter.cicd_service|upper }}" != "TRAVIS":
        remove_file_or_dir(".travis.yml")

    if "{{ cookiecutter.cicd_service|upper }}" != "CIRCLECI":
        remove_file_or_dir(".circleci")

    if "{{ cookiecutter.doc_service }}" != "RTD":
        remove_file_or_dir("readthedocs.yml")

    if "{{ cookiecutter.is_aws_lambda_project }}" != "Y":
        remove_file_or_dir("bin", "lbd")
        remove_file_or_dir("lbd-test-event.json")
        remove_file_or_dir("serverless.yml")
        remove_file_or_dir("{{ cookiecutter.package_name }}/handlers")

    if "{{ cookiecutter.is_aws_cloudformation_project }}" != "Y":
        remove_file_or_dir("{{ cookiecutter.package_name }}/cf")

    print(help_msg)
