# -*- coding: utf-8 -*-


help: ## ** Show this help message
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'


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
test: pip-dev-install req-test ## ** Run test
	bash ./bin/py/test.sh


test-only: ## Run test without checking test dependencies
	bash ./bin/py/test.sh


cov: pip-dev-install req-test ## ** Run Code Coverage test
	bash ./bin/py/test-cov.sh


cov-only: ## Run Code Coverage test without checking test dependencies
	bash ./bin/py/test-cov.sh


tox: ## Run multi python version test with tox
	bash ./bin/py/test-tox.sh


#--- Document ---
build-doc-only: ## Build Documents, skip check doc dependencies, skip clean existing doc
	bash ./bin/py/build-doc-only.sh


build-doc: req-doc pip-dev-install ## ** Build Documents, start over
	bash ./bin/py/build-doc.sh


view-doc: ## ** Open Html Document
	bash ./bin/py/view-doc.sh


deploy-doc-to-version: ## Deploy Html Document to the "x.x.x" version directory on AWS S3
	bash ./bin/py/deploy-doc-to-version.sh


deploy-doc-to-latest: ## Deploy Html Document to the "latest" directory on AWS S3
	bash ./bin/py/deploy-doc-to-latest.sh


deploy-doc: ## ** Deploy Html Document to both "x.x.x" and "latest" directory on AWS S3
	bash ./bin/py/deploy-doc.sh


build-and-deploy-doc: build-doc deploy-doc ## ** Build and deploy Html Document to AWS S3


clean-doc: ## ** Deploy Html Document to AWS S3
	bash ./bin/py/clean-doc.sh


#--- Other ---
reformat: req-dev ## ** Pep8 Format Python Source Code
	bash ./bin/py/reformat-python-code.sh


publish: req-dev ## ** Publish This Package to PyPI
	bash ./bin/py/publish-to-pypi.sh


notebook: ## ** Run jupyter notebook
	bash ./bin/py/run-notebook.sh


info: ## ** Show information about python, pip in this environment
	bash ./bin/py/info.sh


{%- if cookiecutter.is_aws_lambda_project == "Yes" %}
#--- AWS Lambda ---
lbd-build-deploy-pkg: ## Build lambda deployment package
	bash ./bin/py/build-lbd-deploy-pkg.sh


lbd-upload-deploy-pkg: ## Upload lambda deployment package to s3
	bash ./bin/py/upload-lbd-deploy-pkg.sh


lbd-build-and-upload-deploy-pkg: lbd-build-deploy-pkg lbd-upload-deploy-pkg ## Build and upload lambda deployment package to s3
{%- endif %}
