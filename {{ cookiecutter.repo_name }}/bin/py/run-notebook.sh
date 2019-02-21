#!/bin/bash
# -*- coding: utf-8 -*-
#
# Run Jupyter notebook

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] Run Jupyter Notebook locally ..."
${BIN_PIP} install jupyter
${BIN_JUPYTER} notebook
