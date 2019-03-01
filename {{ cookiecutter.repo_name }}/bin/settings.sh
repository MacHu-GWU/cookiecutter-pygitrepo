#!/bin/bash
# -*- coding: utf-8 -*-
#
# This script should be sourced to use.
#
# This file is generated by cookiecutter-pygitrepo {{ cookiecutter._cookiecutter_pygitrepo_version }}: https://github.com/MacHu-GWU/cookiecutter-pygitrepo/tree/{{ cookiecutter._cookiecutter_pygitrepo_version }}


# GitHub
github_account="{{ cookiecutter.github_username }}"
github_repo_name="{{ cookiecutter.repo_name }}"


# Python
package_name="{{ cookiecutter.package_name }}"
py_ver_major="{{ cookiecutter._dev_py_ver_major }}"
py_ver_minor="{{ cookiecutter._dev_py_ver_minor }}"
py_ver_micro="{{ cookiecutter._dev_py_ver_micro }}"
use_pyenv="{{ cookiecutter.use_pyenv }}" # "Y" or "N"
supported_py_versions="{{ cookiecutter.supported_python_versions }}" # e.g: "2.7.13 3.6.2"


#--- Doc Build
rtd_project_name="{{ cookiecutter.doc_rtd_project_name }}"

{%- if cookiecutter.doc_service == "s3" %}
# AWS profile name for hosting doc on S3
# should be defined in ~/.aws/credentials
# read https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for more information
aws_profile_doc_host="{{ cookiecutter.doc_host_aws_profile_name }}"

# html doc will be upload to:
# "s3://${S3_BUCKET_DOC_HOST}/docs/${PACKAGE_NAME}/${PACKAGE_VERSION}"
s3_bucket_doc_host="{{ cookiecutter.doc_host_s3_bucket_name }}"
{%- endif %}

{% if cookiecutter.is_aws_lambda_project == "Yes" %}
#--- AWS Lambda
# AWS profile name for deploy lambda function
# should be defined in ~/.aws/credentials
# read https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for more information
aws_profile_for_lambda="{{ cookiecutter.lambda_aws_profile_name }}"

# deployment package file will be upload to:
# "s3://${s3_bucket_lambda_deploy}/lambda/${github_account}/${github_repo_name}/${package_name}-${package_version}.zip"
s3_bucket_lambda_deploy="{{ cookiecutter.lambda_deployment_s3_bucket_name }}"


# Docker
# deployment package will be built in this container
docker_image_for_build="lambci/lambda:build-python3.6"
# this container will be used for testing lambda invoke
docker_image_for_run="lambci/lambda:python3.6"
dir_container_workspace="/var/task"
{%- endif %}
