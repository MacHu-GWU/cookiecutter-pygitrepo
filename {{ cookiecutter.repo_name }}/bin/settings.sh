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
USE_PYENV="Y" # "Y" or "N"
SUPPORTED_PY_VERSIONS="{{ cookiecutter.supported_python_versions }}" # e.g: "2.7.13 3.6.2"


#--- Doc Build
# AWS profile name for hosting doc on S3
# should be defined in ~/.aws/credentials
# read https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for more information
AWS_PROFILE_DOC_HOST="sanhe"

# html doc will be upload to:
# "s3://${S3_BUCKET_DOC_HOST}/docs/${PACKAGE_NAME}/${PACKAGE_VERSION}"
S3_BUCKET_DOC_HOST="sanherabbit.com"


{%- if cookiecutter.is_aws_lambda_project == "Yes" %}
#--- AWS Lambda
# AWS profile name for deploy lambda function
# should be defined in ~/.aws/credentials
# read https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for more information
AWS_PROFILE_FOR_LAMBDA="sanhe"

# deployment package file will be upload to:
# "s3://${S3_BUCKET_LAMBDA_DEPLOY}/lambda/${GITHUB_ACCOUNT}/${GITHUB_REPO_NAME}/${PACKAGE_NAME}-${PACKAGE_VERSION}.zip"
S3_BUCKET_LAMBDA_DEPLOY="sanhe-learn-aws-lambda-with-sls-deploy"


# Docker
DOCKER_IMAGE_FOR_BUILD="lambci/lambda:build-python3.6"
DOCKER_IMAGE_FOR_RUN="lambci/lambda:python3.6"
DIR_CONTAINER_WORKSPACE="/var/task"
{%- endif %}
