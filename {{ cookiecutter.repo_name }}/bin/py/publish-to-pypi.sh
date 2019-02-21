#!/bin/bash
# -*- coding: utf-8 -*-
#
# Publish this Package to https://pypi.org/

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] Publish ${PACKAGE_NAME} to https://pypi.org ..."
rm -r ${DIR_PROJECT_ROOT}/build ${DIR_PROJECT_ROOT}/dist ${DIR_PROJECT_ROOT}/${PACKAGE_NAME}.egg-info
(
    cd ${DIR_PROJECT_ROOT};
    ${BIN_PYTHON} setup.py sdist bdist_wheel --universal;
    ${BIN_TWINE} upload dist/*;
)
rm -r ${DIR_PROJECT_ROOT}/build ${DIR_PROJECT_ROOT}/dist ${DIR_PROJECT_ROOT}/${PACKAGE_NAME}.egg-info
