#!/bin/bash
# -*- coding: utf-8 -*-
#
# Print useful information related to this python git repository.

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

python "${dir_bin}/pgr/pygitrepo_info.py"
