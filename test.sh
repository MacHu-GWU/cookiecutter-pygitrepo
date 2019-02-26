#!/bin/bash
# -*- coding: utf-8 -*-

stop_test_if_failed() {
    if ! [ $? -eq 0 ]; then
        echo "TEST FAILED!"
        exit 1
    fi
}

rm -r learn_cc-project
python ./test.py
cd ./learn_cc-project

make remove
stop_test_if_failed

make clean
stop_test_if_failed

make info
stop_test_if_failed

make up
stop_test_if_failed

make pip-install
stop_test_if_failed

make pip-uninstall
stop_test_if_failed

make pip-dev-install
stop_test_if_failed

make test
stop_test_if_failed

make test-only
stop_test_if_failed

make cov
stop_test_if_failed

make cov-only
stop_test_if_failed

make info
stop_test_if_failed

make build-doc
stop_test_if_failed

make clean-doc
stop_test_if_failed

make req-dev
stop_test_if_failed

make req-test
stop_test_if_failed

make req-doc
stop_test_if_failed

# clean up everything
make remove
stop_test_if_failed

make clean
stop_test_if_failed

printf -- "\e[32mTest Passed!\e[39m\n"
