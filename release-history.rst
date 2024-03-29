.. _release_history:

Release and Version History
==============================================================================


0.0.7 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.6 (2021-07-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- use cottonformation to replace troposphere_mate

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.5 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Re-implement the interactive repo initialization script. Allows complex inter-option dependency logic which is not available in ``cookiecutter``
- If you are not using ``pyenv-virtualenv``, allows to activate virtualenv with ``source ./bin/py/activate.sh``.
- Add a powerful Centralized config management framework allows you to read and inject config values to any programming language, any system like AWS parameter store. And you can easily customize how's config been dynamically created.
- Add a Deployment on AWS best practice framework allows you to easily manage a multi-env dev/test/prod continues deployment workflow.
- Add CI/CD integration with CircleCI
- improve CI/CD integration with TravisCI

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.2 (2019-02-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- AWS Lambda devops tools with `serverless <https://serverless.com/>`_.
- continues deployment tools with ``make lbd-deploy-all-func``
- local invoke environment with ``bash ./bin/lbd/invoke.sh my_func ./lbd-test-event.json``

**Minor Improvements**

- all shell variable are now lower cased.

**Bugfixes**

- fix ``envlist = py27, py36`` in tox.ini (it was ``envlist = 2.7, 3.6``)

**Miscellaneous**


0.0.1 (2019-02-21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Features and Improvements**

- First release
- Makefile tool
- Virtualenv Integration
- Travis CI Integration
- Codecov Integration
- Sphinx Doc Integration
- Easy doc deploy to ReadTheDocs or AWS S3
- Simple AWS Lambda Deployment Package Build Script
