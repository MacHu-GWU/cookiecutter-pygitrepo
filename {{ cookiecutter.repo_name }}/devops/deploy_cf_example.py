# -*- coding: utf-8 -*-

"""
This is an example about how to deploy CloudFormation and integrate it with
your DevOps automation scripts.
"""

import boto3
from a_micro_service.cf import config, template, param_env_name
from troposphere_mate import StackManager

boto_ses = boto3.session.Session(profile_name=config.AWS_PROFILE_FOR_BOTO3.get_value())

sm = StackManager(boto_ses=boto_ses, cft_bucket=config.S3_BUCKET_FOR_DEPLOY.get_value())

sm.deploy(
    template=template,
    stack_name=config.ENVIRONMENT_NAME.get_value(),
    stack_parameters={
        param_env_name.title: config.ENVIRONMENT_NAME.get_value(),
    },
    include_iam=True
)
