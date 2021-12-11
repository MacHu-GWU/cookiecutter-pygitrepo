# -*- coding: utf-8 -*-

import os
import json
from pathlib_mate import Path
from cookiecutter_pygitrepo.config import Config
from cookiecutter_pygitrepo.helpers import strip_comments

repo_dir = os.getcwd()
path_cookiecutter_pygitrepo_json = Path("{{ cookiecutter.path_cookiecutter_pygitrepo_json }}")
config_data = json.loads(strip_comments(path_cookiecutter_pygitrepo_json.read_text()))
del config_data["_please_ignore_this"]
config = Config(**config_data)

help_msg = """
Things to do next after generated the project skeleton:

- Update ``{{ cookiecutter.repo_name }}/AUTHORS.rst`` file for Author information
- Update ``{{ cookiecutter.repo_name }}/LICENSE.txt`` and ``__license__`` variable in
    ``{{ cookiecutter.repo_name }}/{{ cookiecutter.package_name }}/__init__.py`` (It uses MIT by default).
    If you don't know how to choose an open source license,
    read this https://choosealicense.com/ .
""".strip()
print(help_msg)

msg = """
- If you choose to use CircleCI for CI/CD, you can update the
    ``{{ cookiecutter.repo_name }}/.circleci/config.yml`` file to customize
    CI/CD workflow. The auto-generated one should works out-of the box.
""".strip()
if config.cicd_service == config.CICDServiceEnum.circleci:
    print(msg)

msg = """
- If you choose to use GitHubCI for CI/CD, you can update the
    ``{{ cookiecutter.repo_name }}/.github/workflows/main.yml`` file to customize
    CI/CD workflow. The auto-generated one should works out-of the box.
""".strip()
if config.cicd_service == config.CICDServiceEnum.github:
    print(msg)

msg = """
- If it is a Microservice project on AWS, update the
    ``{{ cookiecutter.repo_name }}/lambda_app/.chalice/config.json`` file 
    to customizeyour microservice settings. And you should implement 
    your microservice logic in ``{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/lbd``
    by yourself. The default code skeleton gives you the best practice
    of microservice development.
""".strip()
if config.is_aws_chalice_project:
    print(msg)

if __name__ == '__main__':
    if config.has_command_line_interface is False:
        Path(repo_dir, config.package_name, "cli.py").remove_if_exists()

    if config.cicd_service != Config.CICDServiceEnum.github:
        Path(repo_dir, ".github", "workflows").remove_if_exists()

    if config.cicd_service != Config.CICDServiceEnum.circleci:
        Path(repo_dir, ".circleci").remove_if_exists()

    if config.doc_service != Config.DocServiceEnum.readthedocs:
        Path(repo_dir, "readthedocs.yml").remove_if_exists()

    if config.is_aws_chalice_project is False:
        Path(repo_dir, "lambda_app").remove_if_exists()
        Path(repo_dir, config.package_name, "lbd").remove_if_exists()
        Path(repo_dir, "bin", "container-only-build-lambda-layer.sh").remove_if_exists()
