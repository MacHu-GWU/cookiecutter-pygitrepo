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


if __name__ == '__main__':

    if "{{ cookiecutter.is_aws_lambda_project }}" != "Yes":
        remove_file_or_dir("bin", "py", "lambda-env.sh")
        remove_file_or_dir("bin", "py", "build-lbd-deploy-pkg.sh")
        remove_file_or_dir("bin", "py", "build-lbd-deploy-pkg-in-container.sh")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        remove_file_or_dir("{{ cookiecutter.package_name }}", "cli.py")
