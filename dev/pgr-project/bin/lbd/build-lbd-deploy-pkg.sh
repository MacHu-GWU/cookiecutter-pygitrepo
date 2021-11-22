#!/bin/bash
# -*- coding: utf-8 -*-
#
# Build lambda deployment package in container locally

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")


aws_lbd_build_docker_img="$(python "${dir_bin}/pgr/pygitrepo.py" "AWS_LAMBDA_BUILD_DOCKER_IMAGE")"

python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}build lambda deployment package at ${path_lambda_deploy_pkg_file} in container ${aws_lbd_build_docker_img} ..."
print_colored_line $color_cyan "[DOING] build lambda deployment package at ${path_lambda_deploy_pkg_file} in container ${aws_lbd_build_docker_img} ..."
mkdir -p ${path_build_lambda_dir}
script_path=${dir_container_workspace}/bin/lbd/build-lbd-deploy-pkg-in-container.sh
docker run -v ${dir_project_root}:${dir_container_workspace} --rm ${docker_image_for_build} bash ${script_path}
