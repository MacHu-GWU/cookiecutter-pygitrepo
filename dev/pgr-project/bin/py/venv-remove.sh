#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

source "${dir_bin}/source/bash_helpers.sh"

dir_venv="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_VENV")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}remove virtualenv at ${dir_venv}"
rm_if_exists "${dir_venv}"
echo "  ${dir_venv} is removed"
