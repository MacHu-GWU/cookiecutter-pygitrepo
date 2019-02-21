#!/bin/bash
# -*- coding: utf-8 -*-
#
# Clean up all temp dir and files (except virtualenv)

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] remove all temp files ..."

tmp_to_remove_list=(
    ${PATH_COVERAGE_ANNOTATE_DIR}
    ${PATH_TOX_DIR}
    ${PATH_BUILD_DIR}
    ${PATH_DIST_DIR}
    ${PATH_EGG_DIR}
    ${PATH_PYTEST_CACHE_DIR}
    ${PATH_SPHINX_DOC_BUILD}
    ${PATH_LAMBDA_DEPLOY_PKG_FILE}
)

for tmp_path in "${tmp_to_remove_list[@]}"
do
    echo "remove ${tmp_path}"
    rm_if_exists ${PATH_COVERAGE_ANNOTATE_DIR}
done
