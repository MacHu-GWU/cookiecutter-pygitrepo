#!/bin/bash
# -*- coding: utf-8 -*-
# Apply pep8 (https://www.python.org/dev/peps/pep-0008/)
# to source code and tests
# using https://pypi.org/project/autopep8

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] reformat python code style, execute ${PATH_AUTO_PEP8_SCRIPT} ..."
${BIN_PYTHON} ${PATH_AUTO_PEP8_SCRIPT}
