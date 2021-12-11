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
    
        - Update ``{{ cookiecutter.repo_name }}/AUTHORS.rst`` file for credit information
        - Update ``{{ cookiecutter.repo_name }}/LICENSE.txt`` and ``__license__`` variable in
            ``{{ cookiecutter.repo_name }}/{{ cookiecutter.package_name }}/__init__.py`` (It uses MIT by default).
            If you don't know how to choose an open source license,
            read this https://choosealicense.com/ .
        - Use ``$ cd ./{{ cookiecutter.repo_name }}`` then ``$ make`` to spin up
            your Python virtual environment for development. Type ``$ make`` for more info.
        {%- if cookiecutter.cicd_service|upper == "TRAVIS" %}
        - If you choose to use TravisCI for CI/CD, you can update the
            ``{{ cookiecutter.repo_name }}/.travis.yml`` file to customize
            CI/CD workflow. The auto-generated one should works out-of the box.
        {%- endif %}
        {%- if cookiecutter.cicd_service|upper == "CIRCLECI" %}
        - If you choose to use CircleCI for CI/CD, you can update the
            ``{{ cookiecutter.repo_name }}/.circleci/config.yml`` file to customize
            CI/CD workflow. The auto-generated one should works out-of the box.
        {%- endif %}
        {%- if cookiecutter.is_aws_project == "Y" %}
        - If it is a AWS project, update ``{{ cookiecutter.repo_name }}/config/00-config-shared.json``
            config file to to use your AWS profile, region, account_id.
        {%- endif %}
        {%- if cookiecutter.is_aws_cloudformation_project == "Y" %}
        - If you need to deploy your app to AWS, update the
            ``{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/cf/__init__.py``
            file to customize the CloudFormation template. And then you can deploy
            from ``{{ cookiecutter.repo_name }}/devops/deploy_cf_example.py`` script.
        {%- endif %}
        {%- if cookiecutter.is_aws_lambda_project == "Y" %}
        - If it is a Microservice project on AWS, update the
            ``{{ cookiecutter.repo_name }}/serverless.yml`` file to customize
            your microservice settings.
            And you should implement your microservice logic in
            ``{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/handlers``
            by your self. The default code skeleton gives you the best practice
            of microservice development.
        {%- endif %}
    """

if __name__ == '__main__':
    if "{{ cookiecutter.has_command_line_interface }}" != "Y":
        remove_file_or_dir("{{ cookiecutter.package_name }}", "cli.py")

    if "{{ cookiecutter.cicd_service|upper }}" != "TRAVIS":
        remove_file_or_dir(".travis.yml")

    if "{{ cookiecutter.cicd_service|upper }}" != "CIRCLECI":
        remove_file_or_dir(".circleci")

    if "{{ cookiecutter.cicd_service|upper }}" != "GITHUB":
        remove_file_or_dir(".github/workflows")

    if "{{ cookiecutter.doc_service|upper }}" != "RTD":
        remove_file_or_dir("readthedocs.yml")

    if "{{ cookiecutter.want_devops_tools }}" != "Y":
        remove_file_or_dir("config")
        remove_file_or_dir("bin/py/config-init.sh")
        remove_file_or_dir("{{ cookiecutter.package_name }}/devops")

    if "{{ cookiecutter.is_aws_cloudformation_project }}" != "Y":
        remove_file_or_dir("{{ cookiecutter.package_name }}/cf")
        remove_file_or_dir("devops", "deploy_cf_example.py")

    if "{{ cookiecutter.is_aws_lambda_project }}" != "Y":
        remove_file_or_dir("{{ cookiecutter.package_name }}/handlers")
        remove_file_or_dir("bin", "lbd")
        remove_file_or_dir("lbd-test-event.json")
        remove_file_or_dir("serverless.yml")

    print(help_msg)
