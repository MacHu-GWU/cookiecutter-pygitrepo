#!/bin/bash
# -*- coding: utf-8 -*-
#
# Python library development bash script tools.
#
# This script should be sourced to use.
#
# This file is generated by cookiecutter-pygitrepo {{ cookiecutter._cookiecutter_pygitrepo_version }}: https://github.com/MacHu-GWU/cookiecutter-pygitrepo/tree/{{ cookiecutter._cookiecutter_pygitrepo_version }}

if [ -n "${BASH_SOURCE}" ]
then
    dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
else
    dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
fi

dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")
source "${dir_bin}/source/bash-helpers.sh"


# Create virtualenv for python package development
venv_up() {
    dir_venv="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_VENV")"
    bin_global_python="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_BIN_GLOBAL_PYTHON")"
    bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"

    pprint "[pygitrepo] {FORE_CYAN}create a virtualenv at {STYLE_RESET_ALL}${dir_venv}"
    if [ -e "${dir_venv}" ]; then
        pprint "[pygitrepo] {FORE_CYAN}  skip, {STYLE_RESET_ALL}${dir_venv} {FORE_CYAN}already exists"
    else
        virtualenv -p "${bin_global_python}" "${dir_venv}"
        "${bin_pip}" install --upgrade pip
        pprint "[pygitrepo] {FORE_CYAN}  done"
    fi
}

# Remove virtualenv
venv_remove() {
    dir_venv="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_VENV")"

    pprint "[pygitrepo] {FORE_CYAN}remove virtualenv at ${dir_venv}"
    if [ -e "${dir_venv}" ]; then
        rm -r "${dir_venv}"
        pprint "[pygitrepo] {FORE_CYAN}  done"
    else
        pprint "[pygitrepo] {FORE_CYAN}  skip, {STYLE_RESET_ALL}${dir_venv} {FORE_CYAN}doesn't exist"
    fi
}

# Install the package to virtualenv in editable mode.
pip_dev_install() {
    package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
    bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"

    pprint "[pygitrepo] {FORE_CYAN}install '${package_name}' to virtualenv in editable mode"
    "${bin_pip}" install --editable "${dir_project_root}"
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Install the package to virtualenv in regular mode.
pip_install() {
    package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
    bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"

    pprint "[pygitrepo] {FORE_CYAN}install '${package_name}' to virtualenv"
    "${bin_pip}" install "${dir_project_root}"
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Uninstall the package from virtualenv.
pip_uninstall() {
    package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
    bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"

    python "${dir_bin}/pgr/pygitrepo_print.py" "[pygitrepo] {FORE_CYAN}uninstall '${package_name}' from virtualenv"
    "${bin_pip}" uninstall -y "${package_name}"
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Install dev dependencies in requirements-dev.txt
req_dev() {
    bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"
    path_req_dev_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_DEV_FILE")"

    pprint "[pygitrepo] {FORE_CYAN}install dependencies in {STYLE_RESET_ALL}requirements-dev.txt {FORE_CYAN}to virtualenv"
    "${bin_pip}" install -r "${path_req_dev_file}"
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Install dev dependencies in requirements-test.txt
req_test() {
    bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"
    path_req_test_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_TEST_FILE")"

    pprint "[pygitrepo] {FORE_CYAN}install dependencies in {STYLE_RESET_ALL}requirements-test.txt {FORE_CYAN}to virtualenv"
    "${bin_pip}" install -r "${path_req_test_file}"
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Install dev dependencies in requirements-doc.txt
req_doc() {
    bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"
    path_req_doc_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_DOC_FILE")"

    pprint "[pygitrepo] {FORE_CYAN}install dependencies in {STYLE_RESET_ALL}requirements-doc.txt {FORE_CYAN}to virtualenv"
    "${bin_pip}" install -r "${path_req_doc_file}"
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Display requirements file content
req_info() {
    path_req_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_FILE")"
    path_req_dev_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_DEV_FILE")"
    path_req_doc_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_DOC_FILE")"
    path_req_test_file="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_REQUIREMENTS_TEST_FILE")"

    pprint "[pygitrepo] {FORE_CYAN}dependencies in {STYLE_RESET_ALL}requirements.txt"
    echo
    cat "${path_req_file}"
    echo

    pprint "[pygitrepo] {FORE_CYAN}dependencies in {STYLE_RESET_ALL}requirements-dev.txt"
    echo
    cat "${path_req_dev_file}"
    echo

    pprint "[pygitrepo] {FORE_CYAN}dependencies in {STYLE_RESET_ALL}requirements-doc.txt"
    echo
    cat "${path_req_doc_file}"
    echo

    pprint "[pygitrepo] {FORE_CYAN}dependencies in {STYLE_RESET_ALL}requirements-test.txt"
    echo
    cat "${path_req_test_file}"
    echo
}

# Run unit test in pytest
test_pytest() {
    bin_pytest="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PYTEST")"
    dir_unit_test="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_UNIT_TESTS")"

    pprint "[pygitrepo] {FORE_CYAN}Run unit test in {STYLE_RESET_ALL}${dir_unit_test}..."
    (
        cd "${dir_project_root}" || exit
        "${bin_pytest}" "${dir_unit_test}" -s
    )
}

# Run coverage in pytest
test_cov() {
    package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
    bin_pytest="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PYTEST")"
    dir_unit_test="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_UNIT_TESTS")"
    dir_coverage_annotate="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_COVERAGE_ANNOTATE")"

    pprint "[pygitrepo] {FORE_CYAN}Run code coverage test in {STYLE_RESET_ALL}${dir_unit_test} ..."
    (
        cd "${dir_project_root}" || exit
        rm_if_exists "${dir_coverage_annotate}"
        "${bin_pytest}" "${dir_unit_test}" -s --cov=${package_name} --cov-report term-missing --cov-report annotate:"${dir_coverage_annotate}"
    )
}

# Run matrix test in tox with pytest, reuse environment,
# only refresh source code and test cases
test_tox_only() {
    bin_pip="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PIP")"
    bin_tox="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_TOX")"
    dir_unit_test="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_UNIT_TESTS")"
    pyenv_local_versions_for_tox="$(python "${dir_bin}/pgr/pygitrepo.py" "PYENV_LOCAL_VERSIONS_FOR_TOX")"

    pprint "[pygitrepo] {FORE_CYAN}Run matrix test with tox ..."
    "${bin_pip}" install tox
    (
        cd "${dir_project_root}" || exit
        pyenv local "${pyenv_local_versions_for_tox}"
        "${bin_tox}"
    )
}

# Run matrix test in tox with pytest, start over, reuse nothing
test_tox() {
    rm_if_exists "${dir_project_root}/.tox"
    test_tox_only
}

# Apply pep8 (https://www.python.org/dev/peps/pep-0008/) to source code and tests
# using https://pypi.org/project/autopep8
reformat_pep8_code_style() {
    bin_python="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PYTHON")"
    pprint "[pygitrepo] {FORE_CYAN}reformat python code style, execute {STYLE_RESET_ALL}${dir_project_root}/fix_code_style.py"
    "${bin_python}" "${dir_project_root}/fix_code_style.py"
}

# Build local documents
build_doc() {
    package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
    dir_sphinx_doc="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC")"
    dir_sphinx_doc_source="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_SOURCE")"
    dir_sphinx_doc_build_html="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD_HTML")"
    bin_activate="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_ACTIVATE")"

    pprint "[pygitrepo] {FORE_CYAN}Build doc at {STYLE_RESET_ALL}${dir_sphinx_doc_build_html}"
    rm_if_exists "${dir_sphinx_doc_build_html}"
    rm_if_exists "${dir_sphinx_doc_source}/${package_name}"
    (
        source "${bin_activate}";
        cd "${dir_sphinx_doc}" || exit;
        make html;
    )
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Build local documents, skip check doc dependencies, skip clean existing doc
build_doc_only() {
    package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
    dir_sphinx_doc="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC")"
    dir_sphinx_doc_build_html="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD_HTML")"
    bin_activate="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_ACTIVATE")"

    pprint "[pygitrepo] {FORE_CYAN}Build doc at {STYLE_RESET_ALL}${dir_sphinx_doc_build_html}"
    rm_if_exists "${dir_sphinx_doc_source}/${package_name}"
    (
        source "${bin_activate}";
        cd "${dir_sphinx_doc}" || exit;
        make html;
    )
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Clear recently built local documents
clean_doc() {
    dir_sphinx_doc_build="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD")"
    dir_sphinx_doc_build_html="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD_HTML")"

    pprint "[pygitrepo] {FORE_CYAN}Clean recently built doc at {STYLE_RESET_ALL}${dir_sphinx_doc_build_html}"
    rm_if_exists "${dir_sphinx_doc_build}"
    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# View recently build local documents
view_doc() {
    open_command="$(python "${dir_bin}/pgr/pygitrepo.py" "OPEN_COMMAND")"
    path_sphinx_doc_build_html_index="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_SPHINX_DOC_BUILD_HTML_INDEX")"

    pprint "[pygitrepo] {FORE_CYAN}open recently built local html doc"
    ${open_command} "${path_sphinx_doc_build_html_index}"
}

# Deploy local html doc to S3 as versioned document
deploy_doc_to_versioned() {
    dir_sphinx_doc_build_html="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD_HTML")"
    s3_uri_doc_dir_versioned="$(python "${dir_bin}/pgr/pygitrepo.py" "S3_URI_DOC_DIR_VERSIONED")"
    url_s3_console_versioned_doc_dir="$(python "${dir_bin}/pgr/pygitrepo.py" "URL_S3_CONSOLE_VERSIONED_DOC_DIR")"
    aws_cli_profile_arg_doc_host="$(python "${dir_bin}/pgr/pygitrepo.py" "AWS_CLI_PROFILE_ARG_DOC_HOST")"

    pprint "[pygitrepo] {FORE_CYAN}deploy doc from local to s3 as versioned doc ..."
    pprint "[pygitrepo] {FORE_CYAN}  aws s3 rm {STYLE_RESET_ALL}${s3_uri_doc_dir_versioned}"
    aws s3 rm "${s3_uri_doc_dir_versioned}" \
        --recursive \
        --only-show-errors \
        --profile "${aws_cli_profile_arg_doc_host}"

    pprint "[pygitrepo] {FORE_CYAN}  aws s3 sync {STYLE_RESET_ALL}${dir_sphinx_doc_build_html} ${s3_uri_doc_dir_versioned}"
    aws s3 sync ${dir_sphinx_doc_build_html} ${s3_uri_doc_dir_versioned} \
        --only-show-errors \
        --profile "${aws_cli_profile_arg_doc_host}"
    pprint "[pygitrepo] {FORE_CYAN}  view versioned doc at {STYLE_RESET_ALL}${url_s3_console_versioned_doc_dir}"
}

# Deploy local html doc to S3 as latest document
deploy_doc_to_latest() {
    dir_sphinx_doc_build_html="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_SPHINX_DOC_BUILD_HTML")"
    s3_uri_doc_dir_latest="$(python "${dir_bin}/pgr/pygitrepo.py" "S3_URI_DOC_DIR_LATEST")"
    url_s3_console_latest_doc_dir="$(python "${dir_bin}/pgr/pygitrepo.py" "URL_S3_CONSOLE_LATEST_DOC_DIR")"
    aws_cli_profile_arg_doc_host="$(python "${dir_bin}/pgr/pygitrepo.py" "AWS_CLI_PROFILE_ARG_DOC_HOST")"

    pprint "[pygitrepo] {FORE_CYAN}deploy doc from local to s3 as latest doc ..."
    pprint "[pygitrepo] {FORE_CYAN}  aws s3 rm {STYLE_RESET_ALL}${s3_uri_doc_dir_latest}"
    aws s3 rm "${s3_uri_doc_dir_latest}" \
        --recursive \
        --only-show-errors \
        --profile "${aws_cli_profile_arg_doc_host}"

    pprint "[pygitrepo] {FORE_CYAN}  aws s3 sync {STYLE_RESET_ALL}${dir_sphinx_doc_build_html} ${s3_uri_doc_dir_latest}"
    aws s3 sync ${dir_sphinx_doc_build_html} ${s3_uri_doc_dir_latest} \
        --only-show-errors \
        --profile "${aws_cli_profile_arg_doc_host}"
    pprint "[pygitrepo] {FORE_CYAN}  view latest doc at {STYLE_RESET_ALL}${url_s3_console_latest_doc_dir}"
}

# Deploy local html doc to S3 as versioned document,
# and also as latest document optionally.
deploy_doc() {
    pprint "[pygitrepo] {FORE_CYAN}deploy doc from local to s3 ..."
    deploy_doc_to_versioned

    pprint "[pygitrepo] {FORE_CYAN}  also deploy latest doc (y/n)?"
    read answer
    if [ "$answer" != "${answer#[Yy]}" ] ;then
        deploy_doc_to_latest
    fi

    pprint "[pygitrepo] {FORE_CYAN}  done"
}

# Publish this Package to https://pypi.org/
publish_to_pypi() {
    package_name="$(python "${dir_bin}/pgr/pygitrepo.py" "PACKAGE_NAME")"
    dir_pypi_build="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_PYPI_BUILD")"
    dir_pypi_dist="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_PYPI_DISTRIBUTE")"
    dir_pypi_egg="$(python "${dir_bin}/pgr/pygitrepo.py" "DIR_PYPI_EGG")"

    bin_python="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_PYTHON")"
    bin_twine="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_TWINE")"

    pprint "[pygitrepo] {FORE_CYAN}Publish ${package_name} to {STYLE_RESET_ALL}https://pypi.org/project/${package_name}/"

    rm_if_exists "${dir_pypi_build}"
    rm_if_exists "${dir_pypi_dist}"
    rm_if_exists "${dir_pypi_egg}"

    (
        cd "${dir_project_root}" || exit;
        ${bin_python} setup.py sdist bdist_wheel --universal;
        ${bin_twine} upload dist/*;
    )
}

# Run Jupyter notebook
run_jupyter() {
    pprint "[pygitrepo] {FORE_CYAN}run jupyter notebook ..."
    bin_jupyter="$(python "${dir_bin}/pgr/pygitrepo.py" "PATH_VENV_BIN_JUPYTER")"
    "${bin_jupyter}" notebook
}
