#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Config:
    GITHUB_ACCOUNT = "MacHu-GWU"
    GITHUB_REPO_NAME = "pgr-project"
    PACKAGE_NAME = "pgr"
    DEV_PY_VER_MAJOR = "3"
    DEV_PY_VER_MINOR = "8"
    DEV_PY_VER_MICRO = "11"
    TOX_TEST_VERSIONS = [
        "2.7.8",
        "3.8.11",
        "3.9.6",
    ]

    # --- Documentation Build
    DOC_HOST_RTD_PROJECT_NAME = "pgr"
    DOC_HOST_AWS_PROFILE = "aws_data_lab_sanhe"
    DOC_HOST_S3_BUCKET = "aws-data-lab-sanhe-for-everything"

    # --- AWS Lambda Related
    AWS_LAMBDA_DEPLOY_AWS_PROFILE = "aws_data_lab_sanhe"
    AWS_LAMBDA_DEPLOY_S3_BUCKET = "aws-data-lab-sanhe-for-everything"
    AWS_LAMBDA_BUILD_DOCKER_IMAGE = "lambci/lambda:build-python3.8"
    AWS_LAMBDA_BUILD_DOCKER_IMAGE_WORKSPACE_DIR = "/var/task"
    AWS_LAMBDA_TEST_DOCKER_IMAGE = "lambci/lambda:python3.8"
