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

#rm -r "${dir_here}/${repo_name}"

#python "${dir_here}/e99_serverless_project.py"

cd "${dir_here}/${repo_name}"

#echo "--- run: make remove"
#make remove
#stop_test_if_failed
#
#echo "--- run: make clean"
#make clean
#stop_test_if_failed

echo "--- run: make info"
make info
stop_test_if_failed

echo "--- run: make up"
make up
stop_test_if_failed

echo "--- run: make pip-dev-install"
make pip-dev-install
stop_test_if_failed

echo "--- run: make req-dev"
make req-dev
stop_test_if_failed

source ./bin/py/activate.sh

pip list


#echo "--- run: make pip-uninstall"
#make pip-uninstall
#stop_test_if_failed
#
#echo "--- run: make pip-dev-install"
#make pip-dev-install
#stop_test_if_failed
#
#echo "--- run: make test"
#make test
#stop_test_if_failed
#
#echo "--- run: make test-only"
#make test-only
#stop_test_if_failed
#
#echo "--- run: make cov"
#make cov
#stop_test_if_failed
#
#echo "--- run: make cov-only"
#make cov-only
#stop_test_if_failed
#
#echo "--- run: make info"
#make info
#stop_test_if_failed
#
#echo "--- run: make build-doc"
#make build-doc
#stop_test_if_failed
#
#echo "--- run: make clean-doc"
#make clean-doc
#stop_test_if_failed
#
#echo "--- run: make req-dev"
#make req-dev
#stop_test_if_failed
#
#echo "--- run: make req-test"
#make req-test
#stop_test_if_failed
#
#echo "--- run: make req-doc"
#make req-doc
#stop_test_if_failed
#
## clean up everything
#echo "--- run: make remove"
#make remove
#stop_test_if_failed
#
#echo "--- run: make clean"
#make clean
#stop_test_if_failed
#
#printf -- "\e[32mTest Passed!\e[39m\n"
