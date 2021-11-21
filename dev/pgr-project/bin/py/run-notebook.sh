#!/bin/bash
# -*- coding: utf-8 -*-
#
# Run Jupyter notebook

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

bin_jupyter="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_JUPYTER")"
aw
"${bin_jupyter}" notebook
