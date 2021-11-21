#!/bin/bash
# -*- coding: utf-8 -*-

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

path_req_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_FILE")"
path_req_dev_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_DEV_FILE")"
path_req_doc_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_DOC_FILE")"
path_req_test_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_TEST_FILE")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}dependencies in requirements.txt"
echo
cat "${path_req_file}"
echo

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}dependencies in requirements-dev.txt"
echo
cat "${path_req_dev_file}"
echo

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}dependencies in requirements-doc.txt"
echo
cat "${path_req_doc_file}"
echo

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}dependencies in requirements-test.txt"
echo
cat "${path_req_test_file}"
echo
