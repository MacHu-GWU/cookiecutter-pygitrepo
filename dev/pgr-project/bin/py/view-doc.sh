#!/bin/bash
# -*- coding: utf-8 -*-
#
# Deploy html doc to s3://${s3-bucket-name}/${doc-dir-prefix}/${package-name}/latest

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

open_command="$(python "${dir_bin}/pgr/pygitrepo.py" "OPEN_COMMAND")"
path_sphinx_doc_build_html_index="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_SPHINX_DOC_BUILD_HTML_INDEX")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}open recently built local html doc"

${open_command} "${path_sphinx_doc_build_html_index}"
