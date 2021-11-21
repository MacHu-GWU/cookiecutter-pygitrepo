#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source "${dir_bin}/source/bash_helpers.sh"

bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"
bin_tox="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_TOX")"
dir_unit_test="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_UNIT_TESTS")"
pyenv_local_versions_for_tox="$(python "${dir_bin}/pgr/pygitrepo.py" "PYENV_LOCAL_VERSIONS_FOR_TOX")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}Run matrix test with tox ..."
"${bin_pip}" install tox
cd "${dir_project_root}" || exit
pyenv local "${pyenv_local_versions_for_tox}"
"${bin_tox}"
