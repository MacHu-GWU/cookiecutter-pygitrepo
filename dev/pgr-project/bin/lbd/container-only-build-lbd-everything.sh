#!/bin/bash
#
# NOTE: This script should be executed INSIDE of the container

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"

source "${dir_bin}/source/aws-lambda.sh"
container_only_build_lbd_everything
