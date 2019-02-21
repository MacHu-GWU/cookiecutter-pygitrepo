#!/bin/bash
# -*- coding: utf-8 -*-

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] Run test in python ${SUPPORTED_PY_VERSIONS} with tox ..."
${BIN_PIP} install tox
cd ${DIR_PROJECT_ROOT}
pyenv local ${SUPPORTED_PY_VERSIONS}
${BIN_TOX}
