#!/bin/bash

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_project_root=$(dirname "${dir_here}")

stage_name="$1"

set -e
python ${dir_here}/switch-env "${stage_name}"
bash ${dir_project_root}/bin/py/config-init.sh
