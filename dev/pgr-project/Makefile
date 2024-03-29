# -*- coding: utf-8 -*-
#
# This file is generated by cookiecutter-pygitrepo {{ cookiecutter._cookiecutter_pygitrepo_version }}: https://github.com/MacHu-GWU/cookiecutter-pygitrepo/tree/{{ cookiecutter._cookiecutter_pygitrepo_version }}

help: ## ** Show this help message
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'


up: ## ** Set Up the Virtual Environment
	bash ./bin/py/venv-up.sh


remove: ## ** Remove Virtual Environment
	bash ./bin/py/venv-remove.sh


clean: ## Clean temp files
	bash ./bin/py/clean.sh


#--- Install ---
pip-uninstall: ## ** Uninstall This Package
	bash ./bin/py/pip-uninstall.sh


pip-install: pip-uninstall ## ** Install This Package via setup.py
	bash ./bin/py/pip-install.sh


pip-dev-install: pip-uninstall ## ** Install This Package in Editable Mode
	bash ./bin/py/pip-dev-install.sh


req-dev: ## Install Development Dependencies
	bash ./bin/py/req-dev.sh


req-doc: ## Install Document Dependencies
	bash ./bin/py/req-doc.sh


req-test: ## Install Test Dependencies
	bash ./bin/py/req-test.sh


#--- Test ---
test: req-test pip-dev-install test-only ## ** Run test


test-only: ## Run test without checking test dependencies
	bash ./bin/py/test.sh


cov: req-test pip-dev-install cov-only ## ** Run Code Coverage test


cov-only: ## Run Code Coverage test without checking test dependencies
	bash ./bin/py/test-cov.sh


tox: ## Run multi python version test with tox
	bash ./bin/py/test-tox.sh


#--- Document ---
build-doc: req-doc pip-dev-install ## ** Build Documents, start over
	bash ./bin/py/build-doc.sh


build-doc-only: ## Build Documents, skip check doc dependencies, skip clean existing doc
	bash ./bin/py/build-doc-only.sh


view-doc: ## ** Open Html Document
	bash ./bin/py/view-doc.sh


deploy-doc-to-version: ## Deploy Html Document to the "x.x.x" version directory on AWS S3
	bash ./bin/py/deploy-doc-to-version.sh


deploy-doc-to-latest: ## Deploy Html Document to the "latest" directory on AWS S3
	bash ./bin/py/deploy-doc-to-latest.sh


deploy-doc: ## ** Deploy Html Document to both "x.x.x" and "latest" directory on AWS S3
	bash ./bin/py/deploy-doc.sh


build-and-deploy-doc: build-doc deploy-doc ## ** Build and deploy Html Document to AWS S3


clean-doc: ## ** Delete recently built Html document
	bash ./bin/py/clean-doc.sh


#--- Other ---
reformat: req-dev ## ** Pep8 Format Python Source Code
	bash ./bin/py/reformat_pep8_code_style.sh


publish: req-dev pip-dev-install ## ** Publish This Package to PyPI
	bash ./bin/py/publish-to-pypi.sh


notebook: ## ** Run jupyter notebook
	bash ./bin/py/run-notebook.sh


info: ## ** Show information about python, pip in this environment
	bash ./bin/py/info.sh


req-info: ## Show requirements information
	bash ./bin/py/req-info.sh


#--- AWS Lambda ---
lbd-build-deploy-pkg: ## Build lambda deployment package
	bash ./bin/lbd/build-lbd-deploy-pkg.sh


lbd-build-layer: ## Build lambda layer
	bash ./bin/lbd/build-lbd-layer.sh


lbd-build-source: ## Build lambda source code
	bash ./bin/lbd/build-lbd-source-code.sh


lbd-build-everything: ## Build lambda deployment package, layer, and source code
	bash ./bin/lbd/build-lbd-everything.sh


lbd-upload-deploy-pkg: ## Upload lambda deployment package to s3
	bash ./bin/lbd/upload-lbd-deploy-pkg.sh


lbd-upload-layer: ## Upload lambda dependencies layer to s3
	bash ./bin/lbd/upload-lbd-layer.sh


lbd-upload-source: ## Upload lambda source code to s3
	bash ./bin/lbd/upload-lbd-source-code.sh


lbd-upload-everything: ## Upload lambda deployment package, layer, and source code to s3
	bash ./bin/lbd/upload-lbd-everything.sh


lbd-deploy-layer: ## Deploy lambda dependencies layer
	bash ./bin/lbd/deploy-lbd-layer.sh


lbd-build-upload-deploy-layer:
	bash ./bin/lbd/build-lbd-layer.sh
	bash ./bin/lbd/upload-lbd-layer.sh
	bash ./bin/lbd/deploy-lbd-layer.sh


lbd-bud-layer: lbd-build-upload-deploy-layer ## Build, upload, deploy lambda dependencies layer
