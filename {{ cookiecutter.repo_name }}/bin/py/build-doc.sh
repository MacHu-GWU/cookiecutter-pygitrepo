#!/bin/bash
# -*- coding: utf-8 -*-

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] Build doc at ${PATH_SPHINX_INDEX_HTML} ..."
rm -r ${PATH_SPHINX_DOC_BUILD}/html
rm -r ${PATH_SPHINX_DOC_SOURCE}/${PACKAGE_NAME}
(
    source ${BIN_ACTIVATE};
    cd ${PATH_SPHINX_DOC};
    make html;
)
