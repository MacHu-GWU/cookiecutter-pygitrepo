# -*- coding: utf-8 -*-

import os
import shutil

REPO_DIR = os.path.dirname(os.path.dirname(__file__))


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
"""


if __name__ == '__main__':

    if "{{ cookiecutter.is_aws_lambda_project }}" != "Yes":
        remove_file_or_dir("bin", "py", "lambda-env.sh")
        remove_file_or_dir("bin", "py", "build-lbd-deploy-pkg.sh")
        remove_file_or_dir("bin", "py", "build-lbd-deploy-pkg-in-container.sh")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        remove_file_or_dir("{{ cookiecutter.package_name }}", "cli.py")

    print(help_msg)
    # help_file = os.path.join(os.path.dirname(__file__), "post-gen-help-info.txt")
    # print(help_file)
    # with open(help_file, "rb") as f:
    #     text = f.read().decode("utf-8")
    #     print(text)

