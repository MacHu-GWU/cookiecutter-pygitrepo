#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

set -e

package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN} uninstall '${package_name}' from virtualenv"

bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"
"${bin_pip}" uninstall -y "${package_name}"
