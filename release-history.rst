.. _release_history:

Release and Version History
==============================================================================


0.0.3 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

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
