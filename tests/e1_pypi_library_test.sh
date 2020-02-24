#!/bin/bash
# -*- coding: utf-8 -*-

stop_test_if_failed() {
    if ! [ $? -eq 0 ]; then
        echo "TEST FAILED!"
        exit 1
    fi
}

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

rm -r "${dir_here}/a_pypi_library-project"

python "${dir_here}/e1_pypi_library.py"

cd "${dir_here}/a_pypi_library-project"

echo "--- run: make remove"
make remove
stop_test_if_failed

echo "--- run: make clean"
make clean
stop_test_if_failed

echo "--- run: make info"
make info
stop_test_if_failed

echo "--- run: make up"
make up
stop_test_if_failed

echo "--- run: make pip-install"
make pip-install
stop_test_if_failed

echo "--- run: make pip-uninstall"
make pip-uninstall
stop_test_if_failed

echo "--- run: make pip-dev-install"
make pip-dev-install
stop_test_if_failed

echo "--- run: make test"
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
