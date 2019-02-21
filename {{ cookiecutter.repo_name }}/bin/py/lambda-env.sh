#!/bin/bash
# -*- coding: utf-8 -*-
#
# This script should be sourced to use.


DIR_HERE="$( cd "$(dirname "$0")" ; pwd -P )"
DIR_BIN="$(dirname "${DIR_HERE}")"
DIR_PROJECT_ROOT=$(dirname "${DIR_BIN}")

source ${DIR_BIN}/py/python-env.sh

FINAL_LAMBDA_DEPLOY_PKG_FILENAME="${PACKAGE_NAME}-${PACKAGE_VERSION}.zip"
PATH_BUILD_LAMBDA_DIR=${PATH_BUILD_DIR}/lambda

# deployment package zip file will be put here on your local machine
PATH_LAMBDA_DEPLOY_PKG_FILE=${PATH_BUILD_LAMBDA_DIR}/${FINAL_LAMBDA_DEPLOY_PKG_FILENAME}

S3_KEY_LAMBDA_DEPLOY_PKG_FILE="lambda/${GITHUB_ACCOUNT}/${GITHUB_REPO_NAME}/${FINAL_LAMBDA_DEPLOY_PKG_FILENAME}"
S3_URI_LAMBDA_DEPLOY_PKG_FILE="s3://${S3_BUCKET_LAMBDA_DEPLOY}/${S3_KEY_LAMBDA_DEPLOY_PKG_FILE}"


upload_deployment_package() {
    aws s3 cp ${PATH_LAMBDA_DEPLOY_PKG_FILE} ${S3_URI_LAMBDA_DEPLOY_PKG_FILE} --profile ${AWS_PROFILE}
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
    local TMP_FUNCTION_NAME=$1 # function name
    echo "${PACKAGE_NAME}.handlers.${TMP_FUNCTION_NAME}.handler"
}


create_function() {
    local TMP_FUNCTION_NAME=$1
    local TMP_EXECUTION_ROLE=$2

    TMP_HANDLER=$(get_handler ${TMP_FUNCTION_NAME})
    aws lambda create-function \
        --function-name ${TMP_FUNCTION_NAME} \
        --runtime "python${PY_VER_MAJOR}.${PY_VER_MINOR}" \
        --role ${TMP_EXECUTION_ROLE} \
        --handler ${TMP_HANDLER} \
        --code "S3Bucket=${S3_BUCKET_LAMBDA_DEPLOY},S3Key=${S3_KEY_LAMBDA_DEPLOY_PKG_FILE}" \
        --timeout 3 \
        --memory-size 128 \
        --environment Variables="{KeyName1=string1,KeyName2=string2}" \
        --profile ${AWS_PROFILE}
}


update_function_code() {
    local TMP_FUNCTION_NAME=$1

    aws lambda update-function-code \
        --function-name ${TMP_FUNCTION_NAME} \
        --s3-bucket ${S3_BUCKET_LAMBDA_DEPLOY} \
        --s3-key ${S3_KEY_LAMBDA_DEPLOY_PKG_FILE} \
        --profile ${AWS_PROFILE}
}


deploy_function() {
    local TMP_FUNCTION_NAME=$1
    local TMP_EXECUTION_ROLE=$2

    tmp=$(aws lambda get-function --function-name ${TMP_FUNCTION_NAME} --profile ${AWS_PROFILE})
    if [ $? -eq 0 ]; then
        update_function_code ${TMP_FUNCTION_NAME}
    else
        create_function ${TMP_FUNCTION_NAME} ${TMP_EXECUTION_ROLE}
    fi
}
