#!/bin/bash
#
# NOTE: This script should be executed INSIDE of the container

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh

print_colored_line $color_cyan "[DOING] upload deployment package at ${path_lambda_deploy_pkg_file}..."
upload_lbd_deployment_package
