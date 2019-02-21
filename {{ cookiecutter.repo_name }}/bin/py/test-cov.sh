#!/bin/bash
# -*- coding: utf-8 -*-

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] Run code coverage tests in ${PATH_TEST_DIR} ..."
cd ${DIR_PROJECT_ROOT}
rm -r ${PATH_COVERAGE_ANNOTATE_DIR}
${BIN_PYTEST} ${PATH_TEST_DIR} -s --cov=${PACKAGE_NAME} --cov-report term-missing --cov-report annotate:${PATH_COVERAGE_ANNOTATE_DIR}
