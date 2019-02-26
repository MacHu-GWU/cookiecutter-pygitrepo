#!/bin/bash
# -*- coding: utf-8 -*-
#
# This script should be sourced to use.


dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/py/python-env.sh

layer_name="${package_name}"
path_build_lambda_dir="${path_build_dir}/lambda"
path_run_lambda_site_packages="${path_build_dir}/lambda/site-packages"


# AWS Lambda now support layers, aws highly recommend that zip dependencies
# as a layer, and only upload source code in your CI / CD
# deployment package, dependencies layer, source code zip will be put here
path_lambda_deploy_pkg_file=${path_build_lambda_dir}/deploy-pkg.zip
path_lambda_source_file=${path_build_lambda_dir}/source.zip
path_lambda_layer_file=${path_build_lambda_dir}/layer.zip


aws_console_url_s3_lambda_deploy="https://s3.console.aws.amazon.com/s3/buckets/${s3_bucket_lambda_deploy}/lambda/${github_account}/${github_repo_name}/"
s3_key_lambda_deploy_repo_root="lambda/${github_account}/${github_repo_name}"

s3_key_lambda_deploy_pkg_file="${s3_key_lambda_deploy_repo_root}/deploy-pkg/${package_version}.zip"
s3_uri_lambda_deploy_pkg_file="s3://${s3_bucket_lambda_deploy}/${s3_key_lambda_deploy_pkg_file}"

s3_key_lambda_source_file="${s3_key_lambda_deploy_repo_root}/source/${package_version}.zip"
s3_uri_lambda_source_file="s3://${s3_bucket_lambda_deploy}/${s3_key_lambda_source_file}"

s3_key_lambda_layer_file="${s3_key_lambda_deploy_repo_root}/layer/${package_version}.zip"
s3_uri_lambda_layer_file="s3://${s3_bucket_lambda_deploy}/${s3_key_lambda_layer_file}"


build_lbd_deployment_package() {
    print_colored_line $color_cyan "create deploy package"
    ensure_not_exists ${path_lambda_deploy_pkg_file}
    ensure_not_exists ${path_run_lambda_site_packages}
    print_colored_line $color_cyan "  zip everything in ${dir_venv_site_packages}"
    cd ${dir_venv_site_packages}
    zip ${path_lambda_deploy_pkg_file} * -r -9 -q -x boto3\* botocore\* setuptools\* easy_install.py pip\* wheel\* twine\* _pytest\* pytest\*;
    print_colored_line $color_cyan "  copy ${dir_venv_site_packages} to ${path_run_lambda_site_packages}"
    cp -r ${dir_venv_site_packages} ${path_run_lambda_site_packages}
}


upload_lbd_deployment_package() {
    if [ -e $path_lambda_deploy_pkg_file ]; then
        aws s3 cp ${path_lambda_deploy_pkg_file} ${s3_uri_lambda_deploy_pkg_file} \
            --profile ${aws_profile_for_lambda}
    else
        print_colored_line $color_light_red "${path_lambda_deploy_pkg_file} not found"
    fi
}


build_lbd_dependencies_layer() {
    print_colored_line $color_cyan "create dependencies layer"
    ensure_not_exists ${path_lambda_layer_file}
    print_colored_line $color_cyan "  zip everything in ${dir_venv_site_packages} except ${package_name}"
    cd ${dir_venv_site_packages}
    zip ${path_lambda_layer_file} * -r -9 -q -x boto3\* botocore\* setuptools\* easy_install.py pip\* wheel\* twine\* _pytest\* pytest\* ${package_name}\*;
}


upload_lbd_dependencies_layer() {
    if [ -e $path_lambda_layer_file ]; then
        aws s3 cp ${path_lambda_layer_file} ${s3_uri_lambda_layer_file} \
            --profile ${aws_profile_for_lambda}
    else
        print_colored_line $color_light_red "${path_lambda_layer_file} not found"
    fi
}


build_lbd_source_code() {
    print_colored_line $color_cyan "create source code zip"
    ensure_not_exists ${path_lambda_source_file}
    print_colored_line $color_cyan "  zip ${package_name} source code"
    cd ${dir_project_root}
    zip ${path_lambda_source_file} ${package_name} -r -9 -q -x __pycache__\* \*.pyc \*.pyd \*.pyo;
}


upload_lbd_source_code() {
    if [ -e $path_lambda_source_file ]; then
        aws s3 cp ${path_lambda_source_file} ${s3_uri_lambda_source_file} \
            --profile ${aws_profile_for_lambda}
    else
        print_colored_line $color_light_red "${path_lambda_source_file} not found"
    fi
}


# upload deployment package, dependencies layer, source code zip to s3
upload_lbd_deployment_everything() {
    upload_lbd_deployment_package
    upload_lbd_dependencies_layer
    upload_lbd_source_code
}


deploy_layer() {
    aws lambda publish-layer-version \
        --layer-name ${layer_name} \
        --description "layer for functions in ${layer_name}" \
        --content "S3Bucket=${s3_bucket_lambda_deploy},S3Key=${s3_key_lambda_layer_file}" \
        --compatible-runtimes "python${py_version_major_and_minor}" \
        --profile ${aws_profile_for_lambda}
}


# AWS CLI wrappers
get_role_arn() {
    local tmp_role_name=$1
    if [ -z "${tmp_role_name}" ]; then
        print_colored_line ${color_red} "role name is required! usage: get_role_arn \"role-name\""
        exit 1
    fi
    aws iam list-roles \
            --profile ${aws_profile_for_lambda} | jq ".Roles[] | select(.RoleName == \"$tmp_role_name\").Arn"
}


get_layer_arn() {
    local tmp_layer_name=$1
    if [ -z "${tmp_layer_name}" ]; then
        print_colored_line ${color_red} "layer name is required! usage: get_layer_arn \"layer-name\""
        exit 1
    fi
    aws lambda list-layers \
        --profile ${aws_profile_for_lambda} | jq ".Layers[] | select(.LayerName == \"$tmp_layer_name\") | .LatestMatchingVersion.LayerVersionArn"
}


get_lambda_exec_role() {
    get_role_arn ${package_name}
}


get_latest_layer_arn() {
    get_layer_arn ${layer_name}
}


# Get the full name of the lambda function handler
# In this pattern, the real handler name is:
# ${PACKAGE_NAME}.handlers.${FUNCTION_NAME}.handler
# it is a function named "def handler(event, context): ..."
# in ${PACKAGE_NAME}.handlers.${FUNCTION_NAME}.py
#
# usage:
#
#   handler=$(get_handler ${func_name})
get_handler() {
    local test_function_name=$1 # function name
    echo "${package_name}.handlers.${test_function_name}.handler"
}


# Run lambda function in container locally with custom event data
#
# usage:
#
#   invoke_lbd "func_name" "path-to-event-json-file.json"
invoke_lbd() {
    local tmp_func_name=$1
    local tmp_event_json_file=$2

    if ! [ -e "${path_run_lambda_site_packages}" ]; then
        print_colored_line $color_red "${path_run_lambda_site_packages} not exits!"
        print_colored_line $color_red "do: \"make lbd-build-deploy-pkg\" first!"
        exit 1
    fi

    if [ -z "${tmp_func_name}" ]; then
        print_colored_line $color_red "function name is required!"
        exit 1
    fi

    # run without event data
    if [ -z "${tmp_event_json_file}" ]; then
        docker run -v ${path_run_lambda_site_packages}:${dir_container_workspace} --rm ${docker_image_for_run} $(get_handler ${tmp_func_name})
    else
        # run with event data in json
        if [ -e "${tmp_event_json_file}" ]; then
            cat ${tmp_event_json_file} | docker run -v ${path_run_lambda_site_packages}:${dir_container_workspace} -i -e DOCKER_LAMBDA_USE_STDIN=1 --rm ${docker_image_for_run} $(get_handler ${tmp_func_name})
        # print helpful info
        else
            print_colored_line $color_red "${tmp_event_json_file} not exists!"
        fi
    fi
}


# Handy deploy function without using serverless
create_function() {
    local test_function_name=$1
    local tmp_execution_role=$2

    tmp_handler=$(get_handler ${test_function_name})
    aws lambda create-function \
        --function-name ${test_function_name} \
        --runtime "python${py_ver_major}.${py_ver_minor}" \
        --role ${tmp_execution_role} \
        --handler ${tmp_handler} \
        --code "S3Bucket=${s3_bucket_lambda_deploy},S3Key=${s3_key_lambda_deploy_pkg_file}" \
        --timeout 3 \
        --memory-size 128 \
        --environment Variables="{KeyName1=string1,KeyName2=string2}" \
        --profile ${aws_profile_for_lambda}
}


update_function_code() {
    local tmp_function_name=$1

    aws lambda update-function-code \
        --function-name ${tmp_function_name} \
        --s3-bucket ${s3_bucket_lambda_deploy} \
        --s3-key ${s3_key_lambda_deploy_pkg_file} \
        --profile ${aws_profile_for_lambda}
}


deploy_function() {
    local tmp_function_name=$1
    local tmp_execution_role=$2

    tmp=$(aws lambda get-function --function-name ${tmp_function_name} --profile ${aws_profile_for_lambda})
    if [ $? -eq 0 ]; then
        update_function_code ${tmp_function_name}
    else
        create_function ${tmp_function_name} ${tmp_execution_role}
    fi
}