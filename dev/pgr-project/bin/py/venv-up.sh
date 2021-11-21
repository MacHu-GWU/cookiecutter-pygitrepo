#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

dir_venv="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_VENV")"
bin_global_python="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_BIN_GLOBAL_PYTHON")"
bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}create a virtualenv at ${dir_venv}"
if [ -e "${dir_venv}" ]; then
    echo "  skip, ${dir_venv} already exists"
else
    virtualenv -p "${bin_global_python}" "${dir_venv}"
    "${bin_pip}" install --upgrade pip
fi
