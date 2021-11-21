#!/bin/bash
# -*- coding: utf-8 -*-
#
# Clear recently built local Documents

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

source "${dir_bin}/source/bash_helpers.sh"

dir_sphinx_doc_build="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD")"
dir_sphinx_doc_build_html="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD_HTML")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}Clean recently built doc at ${dir_sphinx_doc_build_html}"
#rm_if_exists "${dir_sphinx_doc_build}"
