#!/bin/bash
# -*- coding: utf-8 -*-
#
# This script should be sourced to use.

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/settings.sh
source ${DIR_BIN}/lib/detect-os.sh
source ${DIR_BIN}/lib/helpers.sh


# Virtualenv Name
VENV_NAME="${PACKAGE_NAME}_venv"

# Full Python Version
PY_VERSION="${PY_VER_MAJOR}.${PY_VER_MINOR}.${PY_VER_MICRO}"
PY_VERSION_MAJOR_AND_MINOR="${PY_VER_MAJOR}.${PY_VER_MINOR}"


resolve_important_path()
{
    local TMP_DIR_PROJECT_ROOT=$1

    PATH_README=${TMP_DIR_PROJECT_ROOT}/README.rst

    PATH_SPHINX_DOC=${TMP_DIR_PROJECT_ROOT}/docs
    PATH_SPHINX_DOC_SOURCE=${TMP_DIR_PROJECT_ROOT}/docs/source
    PATH_SPHINX_DOC_BUILD=${TMP_DIR_PROJECT_ROOT}/docs/build

    PATH_SPHINX_DOC_BUILD_HTML=${PATH_SPHINX_DOC_BUILD}/html
    PATH_SPHINX_INDEX_HTML=${PATH_SPHINX_DOC_BUILD}/html/index.html

    PATH_SPHINX_CONFIG=${PATH_SPHINX_DOC_SOURCE}/conf.py

    PATH_VERSION_FILE=${TMP_DIR_PROJECT_ROOT}/${PACKAGE_NAME}/_version.py

    PATH_REQUIREMENT_FILE=${TMP_DIR_PROJECT_ROOT}/requirements.txt
    PATH_DEV_REQUIREMENT_FILE=${TMP_DIR_PROJECT_ROOT}/requirements-dev.txt
    PATH_DOC_REQUIREMENT_FILE=${TMP_DIR_PROJECT_ROOT}/requirements-doc.txt
    PATH_TEST_REQUIREMENT_FILE=${TMP_DIR_PROJECT_ROOT}/requirements-test.txt

    PATH_TEST_DIR=${TMP_DIR_PROJECT_ROOT}/tests
    PATH_COVERAGE_ANNOTATE_DIR=${TMP_DIR_PROJECT_ROOT}/.coverage.annotate
    PATH_TOX_DIR=${TMP_DIR_PROJECT_ROOT}/.tox

    PATH_AUTO_PEP8_SCRIPT=${TMP_DIR_PROJECT_ROOT}/fix_code_style.py

    PATH_BUILD_DIR=${TMP_DIR_PROJECT_ROOT}/build
    PATH_DIST_DIR=${TMP_DIR_PROJECT_ROOT}/dist
    PATH_EGG_DIR=${TMP_DIR_PROJECT_ROOT}/${PACKAGE_NAME}.egg-info
    PATH_PYTEST_CACHE_DIR=${TMP_DIR_PROJECT_ROOT}/.pytest_cache
}

resolve_important_path ${DIR_PROJECT_ROOT}


resolve_venv_bin()
{
    # python virtual environment bin directory
    local TMP_DIR_VENV_BIN=$1

    BIN_ACTIVATE="${TMP_DIR_VENV_BIN}/activate"
    BIN_PYTHON="${TMP_DIR_VENV_BIN}/python"
    BIN_PIP="${TMP_DIR_VENV_BIN}/pip"
    BIN_PYTEST="${TMP_DIR_VENV_BIN}/pytest"
    BIN_SPHINX_START="${TMP_DIR_VENV_BIN}/sphinx-quickstart"
    BIN_TWINE="${TMP_DIR_VENV_BIN}/twine"
    BIN_TOX="${TMP_DIR_VENV_BIN}/tox"
    BIN_JUPYTER="${TMP_DIR_VENV_BIN}/jupyter"
    BIN_AWS="${TMP_DIR_VENV_BIN}/aws"
}


resolve_other_venv_dir_on_windows()
{
    # python virtual environment directory
    local TMP_DIR_VENV=$1

    DIR_VENV_BIN="${TMP_DIR_VENV}/Scripts"
    DIR_VENV_SITE_PACKAGES="${TMP_DIR_VENV}/Lib/site-packages"
    DIR_VENV_SITE_PACKAGES64="${TMP_DIR_VENV}/Lib64/site-packages"
}


resolve_other_venv_dir_on_darwin_or_linux()
{
    # python virtual environment directory
    local TMP_DIR_VENV=$1
    # python major and minor version, example: 2.7 or 3.6
    local TMP_PY_VERSION_MAJOR_AND_MINOR=$2

    DIR_VENV_BIN="${TMP_DIR_VENV}/bin"
    DIR_VENV_SITE_PACKAGES="${TMP_DIR_VENV}/lib/python${TMP_PY_VERSION_MAJOR_AND_MINOR}/site-packages"
    DIR_VENV_SITE_PACKAGES64="${TMP_DIR_VENV}/lib64/python${TMP_PY_VERSION_MAJOR_AND_MINOR}/site-packages"
}


# --- resolve venv
resolve_windows_venv()
{
    local TMP_VENV_NAME=$1
    local TMP_PY_VERSION_MAJOR_AND_MINOR=$2

    local TMP_DIR_ENVS="${HOMEPATH}/venvs/python/${TMP_PY_VERSION_MAJOR_AND_MINOR}"
    mkdir -p ${TMP_DIR_ENVS}
    DIR_VENV="${TMP_DIR_ENVS}/${TMP_VENV_NAME}"
    resolve_other_venv_dir_on_windows ${DIR_VENV}
    resolve_venv_bin ${DIR_VENV_BIN}
}


resolve_mac_pyenv()
{
    local TMP_VENV_NAME=$1
    local TMP_PY_VERSION=$2
    local TMP_PY_VERSION_MAJOR_AND_MINOR=$3

    DIR_VENV="${HOME}/.pyenv/versions/${TMP_PY_VERSION}/envs/${TMP_VENV_NAME}"
    resolve_other_venv_dir_on_darwin_or_linux ${DIR_VENV} ${TMP_PY_VERSION_MAJOR_AND_MINOR}
    resolve_venv_bin ${DIR_VENV_BIN}
}


resolve_mac_venv()
{
    local TMP_VENV_NAME=$1
    local TMP_PY_VERSION=$2
    local TMP_PY_VERSION_MAJOR_AND_MINOR=$3

    local TMP_DIR_ENVS="${HOME}/venvs/python/${TMP_PY_VERSION}"
    mkdir -p ${TMP_DIR_ENVS}
    DIR_VENV="${TMP_DIR_ENVS}/${TMP_VENV_NAME}"
    resolve_other_venv_dir_on_darwin_or_linux ${DIR_VENV} ${TMP_PY_VERSION_MAJOR_AND_MINOR}
    resolve_venv_bin ${DIR_VENV_BIN}
}


resolve_linux_venv()
{
    resolve_mac_venv $1 $2 $3
}


if [ "${OS_IS_WINDOWS}" = "Y" ]
then
    BIN_GLOBAL_PYTHON="/c/Python${PY_VER_MAJOR}${PY_VER_MINOR}/python.exe"
    resolve_windows_venv ${VENV_NAME} ${PY_VERSION_MAJOR_AND_MINOR}
elif [ "${OS_IS_DARWIN}" = "Y" ]
then
    BIN_GLOBAL_PYTHON="${HOME}/.pyenv/versions/${PY_VERSION}/bin/python"
    if [ "$USE_PYENV" = "Y" ]
    then
        resolve_mac_pyenv ${VENV_NAME} ${PY_VERSION} ${PY_VERSION_MAJOR_AND_MINOR}
    else
        resolve_mac_venv ${VENV_NAME} ${PY_VERSION} ${PY_VERSION_MAJOR_AND_MINOR}
    fi

elif [ "${OS_IS_LINUX}" = "Y" ]
then
    BIN_GLOBAL_PYTHON="${HOME}/.pyenv/versions/${PY_VERSION}/bin/python"
    resolve_linux_venv ${VENV_NAME} ${PY_VERSION} ${PY_VERSION_MAJOR_AND_MINOR}
fi


PACKAGE_VERSION=$(python ${PATH_VERSION_FILE})
S3_URI_DOC_VERSIONED="s3://${S3_BUCKET_DOC_HOST}/docs/${PACKAGE_NAME}/${PACKAGE_VERSION}"
S3_URI_DOC_LATEST="s3://${S3_BUCKET_DOC_HOST}/docs/${PACKAGE_NAME}/latest"


# Deploy sphinx generated html doc to s3 bucket
deploy_doc_to_s3() {
    local TMP_PATH_SPHINX_DOC_BUILD_HTML="$1" # html doc dir
    local TMP_S3_URI_DOC="$2" # uri of dir on s3

    echo "remove existing doc on ${TMP_S3_URI_DOC}"
    aws s3 rm ${TMP_S3_URI_DOC} \
        --recursive \
        --only-show-errors \
        --profile ${AWS_PROFILE_DOC_HOST}

    echo "upload doc to ${TMP_S3_URI_DOC}"
    aws s3 sync ${TMP_PATH_SPHINX_DOC_BUILD_HTML} ${TMP_S3_URI_DOC} \
        --only-show-errors \
        --profile ${AWS_PROFILE_DOC_HOST}
}
