# -*- coding: utf-8 -*-

import boto3
from datetime import datetime, timezone
from a_micro_service.devops.config_init import config

boto_ses = boto3.session.Session(
    profile_name=config.AWS_PROFILE_FOR_BOTO3.get_value(),
    region_name=config.AWS_REGION.get_value(),
)
iam = boto_ses.client("iam")

res_get_instance_profile = iam.get_instance_profile(InstanceProfileName="pygitrepo-{}-ec2-instance-profile".format(config.ENVIRONMENT_NAME.get_value()))
create_at = res_get_instance_profile["InstanceProfile"]["CreateDate"]
now = datetime.utcnow()
now = now.replace(tzinfo=timezone.utc)
assert (now - create_at).total_seconds() <= 120 # 2 minutes
