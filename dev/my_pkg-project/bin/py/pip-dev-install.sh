#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root="$(dirname "${dir_bin}")"

set -e

package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN} install '${package_name}' to virtualenv in editable mode"

bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"
"${bin_pip}" install --editable "${dir_project_root}"
