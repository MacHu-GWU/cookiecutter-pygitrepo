#!/bin/bash
# -*- coding: utf-8 -*-
#
# This script should be sourced to use.

# 你要创建 3.6.8 版本的虚拟环境, 那么你必须得有一个基础的 3.6.8 版本的环境.
# GitHub
GITHUB_ACCOUNT="{{ cookiecutter.github_username }}"
GITHUB_REPO_NAME="{{ cookiecutter.repo_name }}"


# Python
PACKAGE_NAME="{{ cookiecutter.package_name }}"
PY_VER_MAJOR="{{ cookiecutter._dev_py_ver_major }}"
PY_VER_MINOR="{{ cookiecutter._dev_py_ver_minor }}"
PY_VER_MICRO="{{ cookiecutter._dev_py_ver_micro }}"
USE_PYENV="{{ cookiecutter.use_pyenv }}" # "Y" or "N"
SUPPORTED_PY_VERSIONS="{{ cookiecutter.supported_python_versions }}" # e.g: "2.7.13 3.6.2"


#--- Doc Build
# AWS profile name for hosting doc on S3
# should be defined in ~/.aws/credentials
# read https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for more information
AWS_PROFILE_DOC_HOST="{{ cookiecutter.doc_host_aws_profile_name }}"

# html doc will be upload to:
# "s3://${S3_BUCKET_DOC_HOST}/docs/${PACKAGE_NAME}/${PACKAGE_VERSION}"
S3_BUCKET_DOC_HOST="{{ cookiecutter.doc_host_s3_bucket_name }}"


{%- if cookiecutter.is_aws_lambda_project == "Yes" %}
#--- AWS Lambda
# AWS profile name for deploy lambda function
# should be defined in ~/.aws/credentials
# read https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for more information
AWS_PROFILE_FOR_LAMBDA="{{ cookiecutter.lambda_aws_profile_name }}"

# deployment package file will be upload to:
# "s3://${S3_BUCKET_LAMBDA_DEPLOY}/lambda/${GITHUB_ACCOUNT}/${GITHUB_REPO_NAME}/${PACKAGE_NAME}-${PACKAGE_VERSION}.zip"
S3_BUCKET_LAMBDA_DEPLOY="{{ cookiecutter.lambda_deployment_s3_bucket_name }}"


# Docker
# deployment package will be built in this container
DOCKER_IMAGE_FOR_BUILD="lambci/lambda:build-python3.6"
# this container will be used for testing lambda invoke
DOCKER_IMAGE_FOR_RUN="lambci/lambda:python3.6"
DIR_CONTAINER_WORKSPACE="/var/task"
{%- endif %}
