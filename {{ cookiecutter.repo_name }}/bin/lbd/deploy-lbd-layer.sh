#!/bin/bash
# -*- coding: utf-8 -*-
#
# Build lambda deployment package in container locally

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh

print_colored_line $color_cyan "[DOING] publish layer from ${s3_uri_lambda_layer_file} ..."
deploy_layer


