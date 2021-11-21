#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")


bin_pytest="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PYTEST")"
dir_unit_test="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_UNIT_TESTS")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}Run unit test in ${dir_unit_test}..."
cd "${dir_project_root}" || exit
"${bin_pytest}" "${dir_unit_test}" -s
