#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source "${dir_bin}/source/bash_helpers.sh"

package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
bin_pytest="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PYTEST")"
dir_unit_test="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_UNIT_TESTS")"
dir_coverage_annotate="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_COVERAGE_ANNOTATE")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}Run code coverage test in ${dir_unit_test} ..."
cd "${dir_project_root}" || exit
rm_if_exists "${dir_coverage_annotate}"
"${bin_pytest}" "${dir_unit_test}" -s --cov=${package_name} --cov-report term-missing --cov-report annotate:"${dir_coverage_annotate}"
