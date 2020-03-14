# -*- coding: utf-8 -*-

"""
A command line tools
"""

import string


class Style(object):
    RED = "\033[31m"  # for error message
    GREEN = "\033[32m"  # for success message
    CYAN = "\033[36m"  # for information
    RESET = "\033[39m"  # reset to default


class Logger(object):
    def info(self, msg):
        print(Style.CYAN + msg + Style.RESET)

    def success(self, msg):
        print(Style.GREEN + msg + Style.RESET)

    def error(self, msg):
        print(Style.RED + msg + Style.RESET)


logger = Logger()


def raise_value_error(msg):
    raise ValueError(Style.RED + msg + Style.RESET)


def raise_type_error(msg):
    raise TypeError(Style.RED + msg + Style.RESET)


class Arguments(object):
    package_name_default = "a_example_package"
    package_name_slug_default = "a-example-package"
    repo_name_default = "a_example_package-project"
    github_username_default = "MacHu-GWU"

    author_name_default = "Mr Sanhe Hu"
    author_email_default = "example@email.com"

    has_command_line_interface_options = ["N", "Y"]
    has_command_line_interface_default = has_command_line_interface_options[0]

    supported_python_versions_default = "3.6.2 3.7.2"

    use_pyenv_options = ["N", "Y"]
    use_pyenv_default = use_pyenv_options[0]

    cicd_service_options = ["NO CI", "TRAVIS", "CIRCLECI"]
    cicd_service_default = cicd_service_options[0]

    doc_service_options = ["NO DOC", "RTD", "S3"]
    doc_service_default = doc_service_options[0]

    rtd_project_name_default = "a_example_package"

    want_devops_tools_options = ["N", "Y"]
    want_devops_tools_default = has_command_line_interface_options[0]

    is_aws_project_options = ["N", "Y"]
    is_aws_project_default = is_aws_project_options[0]

    is_aws_cloudformation_project_options = ["N", "Y"]
    is_aws_cloudformation_project_default = is_aws_cloudformation_project_options[0]

    is_aws_lambda_project_options = ["N", "Y"]
    is_aws_lambda_project_default = is_aws_lambda_project_options[0]

    def __init__(self):
        self.package_name = None
        self.package_name_slug = None
        self.repo_name = None
        self.github_username = None
        self.author_name = None
        self.author_email = None
        self.has_command_line_interface = self.has_command_line_interface_default
        self.supported_python_versions = None
        self.use_pyenv = self.use_pyenv_default
        self.cicd_service = self.cicd_service_default
        self.doc_service = self.doc_service_default
        self.rtd_project_name = None
        self.doc_host_aws_profile_name = None
        self.doc_host_s3_bucket_name = None
        self.want_devops_tools = self.want_devops_tools_default
        self.is_aws_project = self.is_aws_project_default
        self.is_aws_cloudformation_project = self.is_aws_cloudformation_project_default
        self.is_aws_lambda_project = self.is_aws_lambda_project_default
        self.aws_profile_name = None
        self.aws_region = None
        self.deployment_s3_bucket_name = None

    def _process_arg(self, arg_name):
        getattr(self, "input_{}".format(arg_name))()
        getattr(self, "init_{}".format(arg_name))()
        getattr(self, "check_{}".format(arg_name))()

    def input_package_name(self):
        """
        Handling prompt input.
        """
        msg = ("Enter your python PACKAGE NAME, use letters and underscore "
               "[default = {}]: ").format(self.package_name_default)
        self.package_name = input(Style.CYAN + msg + Style.RESET)

    def init_package_name(self):
        """
        Initialize input value.
        """
        if not self.package_name.strip():
            self.package_name = self.package_name_default

    def check_package_name(self):
        """
        Validate input value.
        """
        msg = ("A package name has to start with letter and only use"
               "lowercase and underscore!")
        if self.package_name.lower() != self.package_name:
            logger.error(msg)
            self._process_arg("package_name")
            return

        if self.package_name[0] not in string.ascii_lowercase:
            logger.error(msg)
            self._process_arg("package_name")
            return

    def input_package_name_slug(self):
        self.package_name_slug_default = self.package_name.replace("_", "-")
        msg = ("Enter the SLUGIFIED PACKAGE NAME, use letters and dash "
               "[default = {}]: ".format(self.package_name_slug_default))
        self.package_name_slug = input(Style.CYAN + msg + Style.RESET)

    def init_package_name_slug(self):
        if not self.package_name_slug.strip():
            self.package_name_slug = self.package_name_slug_default

    def check_package_name_slug(self):
        msg = ("A slugified package name has to start with letter and only use"
               "lowercase and dash!")

        if self.package_name_slug.lower() != self.package_name_slug:
            logger.error(msg)
            self._process_arg("package_name_slug")
            return

        if "_" in self.package_name_slug[0]:
            logger.error(msg)
            self._process_arg("package_name_slug")
            return

    def input_repo_name(self):
        self.repo_name_default = "{}-project".format(self.package_name)
        msg = ("Enter the GITHUB REPO NAME"
               "[default = {}]: ".format(self.repo_name_default))
        self.repo_name = input(Style.CYAN + msg + Style.RESET)

    def init_repo_name(self):
        if not self.repo_name.strip():
            self.repo_name = self.repo_name_default

    def check_repo_name(self):
        pass

    def input_github_username(self):
        msg = ("Enter the GITHUB USER NAME"
               "[default = {}]: ".format(self.github_username_default))
        self.github_username = input(Style.CYAN + msg + Style.RESET)

    def init_github_username(self):
        if not self.github_username.strip():
            self.github_username = self.github_username_default

    def check_github_username(self):
        pass

    def input_author_name(self):
        msg = ("use the default MIT LICENSE template."
               "Don't forget to change it later."
               "You can pick one from https://opensource.org/licenses/alphabetical")
        print(Style.CYAN + msg + Style.RESET)
        msg = ("Enter the AUTHOR NAME for License info "
               "[default = {}]: ".format(self.author_name_default))
        self.author_name = input(Style.CYAN + msg + Style.RESET)

    def init_author_name(self):
        if not self.author_name.strip():
            self.author_name = self.author_name_default

    def check_author_name(self):
        pass

    def input_author_email(self):
        msg = ("Enter the AUTHOR EMAIL for License info "
               "[default = {}]: ".format(self.author_email_default))
        self.author_email = input(Style.CYAN + msg + Style.RESET)

    def init_author_email(self):
        if not self.author_email.strip():
            self.author_email = self.author_email_default

    def check_author_email(self):
        pass

    def input_has_command_line_interface(self):
        msg = ("Does your library has COMMAND LINE INTERFACE? "
               "[option = {}, default = {}]: ").format(
            " | ".join(self.has_command_line_interface_options),
            self.has_command_line_interface_default,
        )
        self.has_command_line_interface = input(Style.CYAN + msg + Style.RESET)

    def init_has_command_line_interface(self):
        if self.has_command_line_interface.strip().upper() in ["Y", "YES", "TRUE", "1", 1, True]:
            self.has_command_line_interface = "Y"
        else:
            self.has_command_line_interface = self.has_command_line_interface_default

    def check_has_command_line_interface(self):
        if self.has_command_line_interface not in self.has_command_line_interface_options:
            msg = "Has to be one of {}".format(self.has_command_line_interface_options)
            logger.error(msg)
            self._process_arg("package_name_slug")
            return

    def input_supported_python_versions(self):
        msg = ("Enter the PYTHON VERSIONS you want to SUPPORT, "
               "a CI/CD build matrix will be configured, "
               "you can use pyenv to install multiple python version to test locally. "
               "[default = {}]: ".format(self.supported_python_versions_default))
        self.supported_python_versions = input(Style.CYAN + msg + Style.RESET)

    def init_supported_python_versions(self):
        if not self.supported_python_versions.strip():
            self.supported_python_versions = self.supported_python_versions_default

    def check_supported_python_versions(self):
        try:
            for version in self.supported_python_versions.split(" "):
                chunks = version.split(".")
                assert len(chunks) == 3
                for s in chunks:
                    int(s)
                assert int(chunks[0]) in [2, 3, 4]
        except:
            msg = ('Error: the supported python versions ({}) is invalid, '
                   'valid example: 3.6.2 3.7.2'.format(self.supported_python_versions))
            logger.error(msg)
            self._process_arg("supported_python_versions")
            return

    def input_use_pyenv(self):
        msg = ("Do you prefer to use pyenv-virtualenv to manage VIRTUALENV? "
               "[option = {}, default = {}]: ").format(
            " | ".join(self.use_pyenv_options),
            self.use_pyenv_default,
        )
        self.use_pyenv = input(Style.CYAN + msg + Style.RESET)

    def init_use_pyenv(self):
        if self.use_pyenv.strip().upper() in ["Y", "YES", "TRUE", "1", 1, True]:
            self.use_pyenv = "Y"
        else:
            self.use_pyenv = self.use_pyenv_default

    def check_use_pyenv(self):
        if self.use_pyenv not in self.use_pyenv_options:
            msg = "Has to be one of {}".format(self.use_pyenv_options)
            logger.error(msg)
            self._process_arg("use_pyenv")
            return

    def input_cicd_service(self):
        msg = ("Enter the CI/CD SERVICE you want to use "
               "to automate your build, test and deployment. "
               "For open source pip installable library, I recommend travis. "
               "For a application project, I recommend circleci."
               "[option = {}, default = {}]: ").format(
            " | ".join(self.cicd_service_options).lower(),
            self.cicd_service_default,
        )

        self.cicd_service = input(Style.CYAN + msg + Style.RESET)

    def init_cicd_service(self):
        if not self.cicd_service.strip():
            self.cicd_service = self.cicd_service_default.upper()

    def check_cicd_service(self):
        if self.cicd_service.upper() not in self.cicd_service_options:
            msg = ('Error: the cicd service ({}) is invalid, '
                   'it has to be one of: {}]').format(
                self.cicd_service,
                self.cicd_service_options,
            )
            logger.error(msg)
            self._process_arg("cicd_service")
            return

    def input_doc_service(self):
        msg = ("Enter the DOCUMENTATION HOST SERVICE you want to use,"
               "if you want to automatically extract docs from source code. "
               "For open source project, I recommend www.readthedocs.org (rtd). "
               "For private project, I recommend to deploy to AWS S3."
               "[option = {}, default = {}]: ").format(
            " | ".join(self.doc_service_options).lower(),
            self.doc_service_default,
        )

        self.doc_service = input(Style.CYAN + msg + Style.RESET)

    def init_doc_service(self):
        if not self.doc_service.strip():
            self.doc_service = self.doc_service_default.upper()

    def check_doc_service(self):
        if self.doc_service.upper() not in self.doc_service_options:
            msg = ('Error: the doc service ({}) is invalid, '
                   'it has to be one of: {}]').format(
                self.doc_service,
                self.doc_service_options,
            )
            logger.error(msg)
            self._process_arg("doc_service")
            return

    def input_rtd_project_name(self):
        if self.doc_service.upper() != "RTD":
            return

        self.rtd_project_name_default = self.package_name.replace("_", "-")
        msg = ("Enter the READTHEDOCS PROJECT NAME, "
               "better to reuse your package name "
               "[default = {}]: ".format(self.rtd_project_name_default))
        self.rtd_project_name = input(Style.CYAN + msg + Style.RESET)

    def init_rtd_project_name(self):
        if self.doc_service.upper() != "RTD":
            return

        if not self.rtd_project_name.strip():
            self.rtd_project_name = self.rtd_project_name_default

    def check_rtd_project_name(self):
        if self.doc_service.upper() != "RTD":
            return

    def input_doc_host_aws_profile_name(self):
        if self.doc_service.upper() != "S3":
            return

        msg = ("Enter the AWS PROFILE to upload the doc. "
               "To understand how to configure aws profile, "
               "please read https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html"
               " [required]: ")
        self.doc_host_aws_profile_name = input(Style.CYAN + msg + Style.RESET)

    def init_doc_host_aws_profile_name(self):
        if self.doc_service.upper() != "S3":
            return

        if not self.doc_host_aws_profile_name.strip():
            msg = "doc host aws profile name is required!"
            logger.error(msg)
            self._process_arg("doc_host_aws_profile_name")

    def check_doc_host_aws_profile_name(self):
        if self.doc_service.upper() != "S3":
            return

    def input_doc_host_s3_bucket_name(self):
        if self.doc_service.upper() != "S3":
            return

        msg = ("Enter the S3 BUCKET NAME you want to upload the doc to. "
               "To understand how to host static site on aws, "
               "and only allow access from specific IP address, "
               "please read https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html"
               " [required]: ")
        self.doc_host_s3_bucket_name = input(Style.CYAN + msg + Style.RESET)

    def init_doc_host_s3_bucket_name(self):
        if self.doc_service.upper() != "S3":
            return

        if not self.doc_host_s3_bucket_name.strip():
            msg = "doc host s3 bucket name is required!"
            logger.error(msg)
            self._process_arg("doc_host_s3_bucket_name")

    def check_doc_host_s3_bucket_name(self):
        if self.doc_service.upper() != "S3":
            return

    def input_want_devops_tools(self):
        msg = ("Do you want to include DEVOPS TOOLS? "
               "It helps you to securely manage complex configurations, "
               "and allows multi-environment deployment."
               "[option = {}, default = {}]: ").format(
            " | ".join(self.want_devops_tools_options),
            self.want_devops_tools_default,
        )
        self.want_devops_tools = input(Style.CYAN + msg + Style.RESET)

    def init_want_devops_tools(self):
        if self.want_devops_tools.strip().upper() in ["Y", "YES", "TRUE", "1", 1, True]:
            self.want_devops_tools = "Y"
        else:
            self.want_devops_tools = self.want_devops_tools_default

    def check_want_devops_tools(self):
        if self.want_devops_tools not in self.want_devops_tools_options:
            msg = "Has to be one of {}".format(self.want_devops_tools_options)
            logger.error(msg)
            self._process_arg("want_devops_tools")
            return

    def input_is_aws_project(self):
        msg = ("Is this a AWS project? "
               "[option = {}, default = {}]: ").format(
            " | ".join(self.is_aws_project_options),
            self.is_aws_project_default,
        )
        self.is_aws_project = input(Style.CYAN + msg + Style.RESET)

    def init_is_aws_project(self):
        if self.is_aws_project.strip().upper() in ["Y", "YES", "TRUE", "1", 1, True]:
            self.is_aws_project = "Y"
        else:
            self.is_aws_project = self.is_aws_project_default

    def check_is_aws_project(self):
        if self.is_aws_project not in self.is_aws_project_options:
            msg = "Has to be one of {}".format(self.is_aws_project_options)
            logger.error(msg)
            self._process_arg("is_aws_project")
            return

    def input_is_aws_cloudformation_project(self):
        if self.is_aws_project.upper() != "Y":
            return
        msg = ("Is this a AWS CloudFormation project? "
               "[option = {}, default = {}]: ").format(
            " | ".join(self.is_aws_cloudformation_project_options),
            self.is_aws_cloudformation_project_default,
        )
        self.is_aws_cloudformation_project = input(Style.CYAN + msg + Style.RESET)

    def init_is_aws_cloudformation_project(self):
        if self.is_aws_project.upper() != "Y":
            return
        if self.is_aws_cloudformation_project.strip().upper() in ["Y", "YES", "TRUE", "1", 1, True]:
            self.is_aws_cloudformation_project = "Y"
        else:
            self.is_aws_cloudformation_project = self.is_aws_cloudformation_project_default

    def check_is_aws_cloudformation_project(self):
        if self.is_aws_project.upper() != "Y":
            return
        if self.is_aws_cloudformation_project not in self.is_aws_cloudformation_project_options:
            msg = "Has to be one of {}".format(self.is_aws_cloudformation_project_options)
            logger.error(msg)
            self._process_arg("is_aws_cloudformation_project")
            return

    def input_is_aws_lambda_project(self):
        if self.is_aws_project.upper() != "Y":
            return
        msg = ("Is this a AWS Lambda project? "
               "[option = {}, default = {}]: ").format(
            " | ".join(self.is_aws_lambda_project_options),
            self.is_aws_lambda_project_default,
        )
        self.is_aws_lambda_project = input(Style.CYAN + msg + Style.RESET)

    def init_is_aws_lambda_project(self):
        if self.is_aws_project.upper() != "Y":
            return
        if self.is_aws_lambda_project.strip().upper() in ["Y", "YES", "TRUE", "1", 1, True]:
            self.is_aws_lambda_project = "Y"
        else:
            self.is_aws_lambda_project = self.is_aws_lambda_project_default

    def check_is_aws_lambda_project(self):
        if self.is_aws_project.upper() != "Y":
            return
        if self.is_aws_lambda_project not in self.is_aws_lambda_project_options:
            msg = "Has to be one of {}".format(self.is_aws_lambda_project_options)
            logger.error(msg)
            self._process_arg("is_aws_lambda_project")
            return

    def input_aws_profile_name(self):
        if self.is_aws_project.upper() != "Y":
            return

        msg = ("Enter the AWS PROFILE for DEVELOPMENT and DEPLOYMENT. "
               "To understand how to configure aws profile, "
               "please read https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html"
               " [required]: ")
        self.aws_profile_name = input(Style.CYAN + msg + Style.RESET)

    def init_aws_profile_name(self):
        if self.is_aws_project.upper() != "Y":
            return

        if not self.aws_profile_name.strip():
            msg = "aws profile name is required!"
            logger.error(msg)
            self._process_arg("aws_profile_name")

    def check_aws_profile_name(self):
        if self.is_aws_project.upper() != "Y":
            return

    def input_aws_region(self):
        if self.is_aws_project.upper() != "Y":
            return

        msg = ("Enter the AWS REGION for DEVELOPMENT and DEPLOYMENT. "
               "Example: us-east-1. For full list of AWS REGION, "
               "see https://docs.aws.amazon.com/general/latest/gr/rande.html"
               " [required]: ")
        self.aws_region = input(Style.CYAN + msg + Style.RESET)

    def init_aws_region(self):
        if self.is_aws_project.upper() != "Y":
            return

        if not self.aws_region.strip():
            msg = "aws region name is required!"
            logger.error(msg)
            self._process_arg("aws_region")

    def check_aws_region(self):
        if self.is_aws_project.upper() != "Y":
            return

    def input_aws_account_id(self):
        if self.is_aws_project.upper() != "Y":
            return

        msg = ("Enter the 12 digits AWS ACCOUNT ID for DEVELOPMENT and DEPLOYMENT. "
               "Log in to your AWS Console to view your account id."
               " [required]: ")
        self.aws_account_id = input(Style.CYAN + msg + Style.RESET)

    def init_aws_account_id(self):
        if self.is_aws_project.upper() != "Y":
            return

        if not self.aws_account_id.strip():
            msg = "aws account name is required!"
            logger.error(msg)
            self._process_arg("aws_account_id")

    def check_aws_account_id(self):
        if self.is_aws_project.upper() != "Y":
            return

    def input_deployment_s3_bucket_name(self):
        if not (self.is_aws_cloudformation_project.upper() == "Y"
                or self.is_aws_lambda_project.upper() == "Y"):
            return

        msg = ("Enter the S3 BUCKET NAME you want to use for AWS deployment. "
               "It is for uploading artifacts like cloudformation template, "
               "lambda function deployment package. "
               "I recommend to use '${aws_account_alias}-for-everything'. "
               " [required]: ")
        self.deployment_s3_bucket_name = input(Style.CYAN + msg + Style.RESET)

    def init_deployment_s3_bucket_name(self):
        if not (self.is_aws_cloudformation_project.upper() == "Y"
                or self.is_aws_lambda_project.upper() == "Y"):
            return

        if not self.deployment_s3_bucket_name.strip():
            msg = "deployment s3 bucket name is required!"
            logger.error(msg)
            self._process_arg("deployment_s3_bucket_name")

    def check_deployment_s3_bucket_name(self):
        if not (self.is_aws_cloudformation_project.upper() == "Y"
                or self.is_aws_lambda_project.upper() == "Y"):
            return


def arg_to_dct(arg_class):
    return {k: v for k, v in arg_class.__dict__.items() if not k.startswith("_")}


def init_package_name(value):
    pass


# Arg.package_name = input(Style.CYAN + "Enter your python package name: ")

# check_package_name(Arg.package_name)

# print(Style.RESET)
#
# print(arg_to_dct(Arg))


if __name__ == "__main__":
    import os
    from cookiecutter.main import cookiecutter
    import sys
    from datetime import datetime, date

    args = Arguments()

    for attr in list(args.__dict__):
        args._process_arg(attr)

    # print(args.__dict__)

    dir_here = os.path.dirname(__file__)
    with open(os.path.join(dir_here, "version.txt"), "rb") as f:
        cookiecutter_pygitrepo_version = f.read().decode("utf-8").strip()

    extra_context = dict(
        _dev_py_ver_major=sys.version_info.major,
        _dev_py_ver_minor=sys.version_info.minor,
        _dev_py_ver_micro=sys.version_info.micro,
        _dev_py_ver_full="{}.{}.{}".format(
            sys.version_info.major,
            sys.version_info.minor,
            sys.version_info.micro,
        ),
        _current_year=datetime.now().year,
        _current_date=str(date.today()),
        _cookiecutter_pygitrepo_version=cookiecutter_pygitrepo_version,
    )
    extra_context.update(args.__dict__)

    cookiecutter(
        dir_here,
        extra_context=extra_context,
        no_input=True,
    )
