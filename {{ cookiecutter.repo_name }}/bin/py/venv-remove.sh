#!/bin/bash
# -*- coding: utf-8 -*-

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] remove ${DIR_VENV} for ${VENV_NAME} ..."
if [ ${USE_PYENV} == "Y" ]; then
    pyenv uninstall -f ${VENV_NAME}
else
    rm_if_exists ${DIR_VENV}
fi
