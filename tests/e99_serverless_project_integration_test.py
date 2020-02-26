# -*- coding: utf-8 -*-

import sys, traceback
import boto3
from datetime import datetime, timezone
from a_micro_service.devops.config_init import config

try:
    boto_ses = boto3.session.Session(
        profile_name=config.AWS_PROFILE_FOR_BOTO3.get_value(),
        region_name=config.AWS_REGION.get_value(),
    )
    iam = boto_ses.client("iam")

    res_get_role = iam.get_role(RoleName="pygitrepo-{}-ec2-role".format(config.ENVIRONMENT_NAME.get_value()))
    create_at = res_get_role["Role"]["CreateDate"]
    now = datetime.utcnow()
    now = now.replace(tzinfo=timezone.utc)

    assert (now - create_at).total_seconds() <= 120 # 2 minutes

    cft = boto_ses.client("cloudformation")
    cft.delete_stack(StackName="pygitrepo-{}".format(config.ENVIRONMENT_NAME.get_value()))

    assert 1 == 0
except:
    traceback.print_exc()
    sys.exit(1)
