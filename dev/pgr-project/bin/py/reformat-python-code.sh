#!/bin/bash
# -*- coding: utf-8 -*-
#
# Apply pep8 (https://www.python.org/dev/peps/pep-0008/)
# to source code and tests
# using https://pypi.org/project/autopep8

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

bin_python="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PYTHON")"
python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}reformat python code style, execute ${dir_project_root}/fix_code_style.py"

"${bin_python}" "${dir_project_root}/fix_code_style.py"
