#!/bin/bash
# -*- coding: utf-8 -*-
#
# Install dev dependencies in requirements-test.txt

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}install dependencies in requirements-test.txt to virtualenv"

bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"
path_req_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_TEST_FILE")"
"${bin_pip}" install -r "${path_req_file}"
