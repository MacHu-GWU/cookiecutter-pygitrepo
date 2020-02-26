#!/bin/bash
# -*- coding: utf-8 -*-

stop_test_if_failed() {
    if ! [ $? -eq 0 ]; then
        echo "TEST FAILED!"
        exit 1
    fi
}

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

repo_name="a_micro_service-project"

rm -r "${dir_here}/${repo_name}"

set -e
python "${dir_here}/e99_serverless_project.py"
set +e

cd "${dir_here}/${repo_name}"

echo "--- run: make remove"
make remove
stop_test_if_failed

echo "--- run: make clean"
make clean
stop_test_if_failed

echo "--- run: make info"
make info
stop_test_if_failed

set -e
echo "--- run: make up"
make up
stop_test_if_failed

echo "--- run: make pip-dev-install"
make pip-dev-install
stop_test_if_failed

echo "--- run: make req-dev"
make req-dev
stop_test_if_failed
set +e

echo "--- enter virtualenv"
source ./bin/py/activate.sh

echo "--- switch env to dev"
./config/switch-env dev

set -e
echo "--- deploy app to test AWS account"
python ./devops/deploy_cf_example.py

sleep 30

echo "--- test the deployment, run integration test"
python ../e99_serverless_project_integration_test.py

echo "--- test reading the configs"
python ./devops/read_config_example.py

echo "--- test build lambda source"
make lbd-build-source
