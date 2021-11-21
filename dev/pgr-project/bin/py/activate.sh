#!/bin/bash
# -*- coding: utf-8 -*-
#
# activate / deactivate your virtualenv for this project
# without explicitly passing the path
#
# usage:
#
# - activate: ``$ source ./bin/py/activate.sh``
# - deactivate: ``$ deactivate``

if [ -n "${BASH_SOURCE}" ]
then
    dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
else
    dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
fi
dir_bin="$(dirname "${dir_here}")"

bin_activate="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_ACTIVATE")"

source "${bin_activate}"
