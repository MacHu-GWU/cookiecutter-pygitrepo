# -*- coding: utf-8 -*-

from configirl import ConfigClass, Constant, Derivable


class Config(ConfigClass):
    METADATA = Constant(default=dict(), dont_dump=True)

    PROJECT_NAME = Constant()
    PROJECT_NAME_SLUG = Derivable()

    @PROJECT_NAME_SLUG.getter
    def get_project_name_slug(self):
        return self.PROJECT_NAME.get_value().replace("_", "-")

    STAGE = Constant()  # example dev / test / prod

    ENVIRONMENT_NAME = Derivable()

    @ENVIRONMENT_NAME.getter
    def get_ENVIRONMENT_NAME(self):
        return "{}-{}".format(self.PROJECT_NAME_SLUG.get_value(self), self.STAGE.get_value())

    {%- if cookiecutter.is_aws_project == "Y" %}
    AWS_PROFILE = Constant()

    AWS_PROFILE_FOR_BOTO3 = Derivable()

    @AWS_PROFILE_FOR_BOTO3.getter
    def get_AWS_PROFILE_FOR_BOTO3(self):
        if self.is_aws_ec2_runtime():
            return None
        elif self.is_aws_lambda_runtime():
            return None
        elif self.is_circle_ci_runtime():
            return None
        else: # local computer runtime
            return self.AWS_PROFILE.get_value()

    AWS_REGION = Constant()
    AWS_ACCOUNT_ID = Constant(printable=False)
    {%- endif %}

    {%- if cookiecutter.is_aws_cloudformation_project == "Y" or  cookiecutter.is_aws_lambda_project == "Y" %}
    S3_BUCKET_FOR_DEPLOY = Constant()
    {%- endif %}