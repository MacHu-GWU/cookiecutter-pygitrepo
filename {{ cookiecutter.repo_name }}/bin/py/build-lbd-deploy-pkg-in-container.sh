#!/bin/bash
#
# NOTE: This script should be executed INSIDE of the container

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/lambda-env.sh

resolve_important_path ${DIR_PROJECT_ROOT}
resolve_mac_venv ${VENV_NAME} ${PY_VERSION} ${PY_VERSION_MAJOR_AND_MINOR}

rm -r ${DIR_VENV}
rm -r ${PATH_LAMBDA_DEPLOY_PKG_FILE}

cd ${DIR_PROJECT_ROOT}

print_colored_line $color_cyan "create virtual env at ${DIR_VENV} in container ..."
virtualenv ${DIR_VENV}

print_colored_line $color_cyan "pip install dependencies ..."
${BIN_PIP} install ${DIR_PROJECT_ROOT}

print_colored_line $color_cyan "zip dependencies ..."
cd ${DIR_VENV_SITE_PACKAGES}
zip ${PATH_LAMBDA_DEPLOY_PKG_FILE} * -r -9 -q -x boto3\* botocore\* setuptools\* pip\* wheel\* twine\*_pytest\* pytest\*;

print_colored_line $color_cyan "done"

rm -r ${DIR_VENV}
