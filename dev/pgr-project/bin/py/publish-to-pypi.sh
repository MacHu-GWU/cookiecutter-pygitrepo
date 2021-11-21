#!/bin/bash
# -*- coding: utf-8 -*-
#
# Publish this Package to https://pypi.org/

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source "${dir_bin}/source/bash_helpers.sh"

package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
dir_pypi_build="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_PYPI_BUILD")"
dir_pypi_dist="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_PYPI_DISTRIBUTE")"
dir_pypi_egg="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_PYPI_EGG")"

bin_python="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PYTHON")"
bin_twine="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_TWINE")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}Publish ${package_name} to https://pypi.org ..."

rm_if_exists "${dir_pypi_build}"
rm_if_exists "${dir_pypi_dist}"
rm_if_exists "${dir_pypi_egg}"

(
    cd "${dir_project_root}" || exit;
    ${bin_python} setup.py sdist bdist_wheel --universal;
    ${bin_twine} upload dist/*;
)
