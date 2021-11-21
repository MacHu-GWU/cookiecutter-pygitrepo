#!/bin/bash
# -*- coding: utf-8 -*-
#
# Deploy html doc to s3://${s3-bucket-name}/${doc-dir-prefix}/${package-name}/${version}

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

dir_sphinx_doc_build_html="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD_HTML")"
s3_uri_doc_dir_versioned="$(python "${dir_bin}/pgr/pygitrepo.py" "S3_URI_DOC_DIR_VERSIONED")"
aws_cli_profile_arg_doc_host="$(python "${dir_bin}/pgr/pygitrepo.py" "AWS_CLI_PROFILE_ARG_DOC_HOST")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}deploy versioned doc from local to s3 ..."

echo "aws s3 rm ${s3_uri_doc_dir_versioned}"
aws s3 rm "${s3_uri_doc_dir_versioned}" \
    --recursive \
    --only-show-errors \
    --profile "${aws_cli_profile_arg_doc_host}"

echo "aws s3 sync ${dir_sphinx_doc_build_html} ${s3_uri_doc_dir_versioned}"
aws s3 sync ${dir_sphinx_doc_build_html} ${s3_uri_doc_dir_versioned} \
    --only-show-errors \
    --profile "${aws_cli_profile_arg_doc_host}"

echo "done"
