#!/bin/bash
# -*- coding: utf-8 -*-

DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

print_colored_line $color_cyan "[DOING] print useful information:"
if [ -e ${DIR_VENV} ]; then
    print_colored_line $color_green "virtualenv is ready to use at: ${DIR_VENV}"
else
    print_colored_line $color_red "virtualenv are NOT found at: ${DIR_VENV}"
fi

if [ -z "$(${BIN_PIP} show ${PACKAGE_NAME} | grep "Name:")" ]; then
    print_colored_line $color_red "${PACKAGE_NAME} is NOT installed at: ${DIR_VENV_SITE_PACKAGES}"
else
    print_colored_line $color_green "${PACKAGE_NAME} is installed at: ${DIR_VENV_SITE_PACKAGES}"
fi

printf -- "\n-\e[36m venv:\e[39m ${DIR_VENV}"
printf -- "\n-\e[36m python executable:\e[39m ${BIN_PYTHON}"
printf -- "\n-\e[36m pip executable:\e[39m ${BIN_PIP}"
printf -- "\n-\e[36m site-packages:\e[39m ${DIR_VENV_SITE_PACKAGES}"
printf -- "\n-\e[36m site-packages64:\e[39m ${DIR_VENV_SITE_PACKAGES64}"
printf -- "\n-\e[36m local html doc:\e[39m ${PATH_SPHINX_INDEX_HTML}"
printf -- "\n-\e[36m readme:\e[39m ${PATH_README}"

#echo - document on rtd: ${RTD_DOC_URL}
#echo - document on s3: ${AWS_DOC_URL}

echo ""
