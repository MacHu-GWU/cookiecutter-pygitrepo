#!/bin/bash
# -*- coding: utf-8 -*-

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] pip install ${PATH_DOC_REQUIREMENT_FILE} ..."
${BIN_PIP} install -r ${PATH_DOC_REQUIREMENT_FILE}
