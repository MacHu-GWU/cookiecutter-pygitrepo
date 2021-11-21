#!/bin/bash
# -*- coding: utf-8 -*-
#
# Build local Documents, skip check doc dependencies, skip clean existing doc

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

source "${dir_bin}/source/bash_helpers.sh"

package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
dir_sphinx_doc="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC")"
dir_sphinx_doc_source="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_SOURCE")"
dir_sphinx_doc_build_html="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD_HTML")"
bin_activate="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_ACTIVATE")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}Build doc at ${dir_sphinx_doc_build_html}"
rm_if_exists "${dir_sphinx_doc_source}/${package_name}"
(
    source "${bin_activate}";
    cd "${dir_sphinx_doc}" || exit;
    make html;
)
