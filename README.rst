
.. image:: https://circleci.com/gh/MacHu-GWU/cookiecutter-pygitrepo/tree/master.svg?style=svg
    :target: https://circleci.com/gh/MacHu-GWU/cookiecutter-pygitrepo/tree/master

------

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/MacHu-GWU/cookiecutter-pygitrepo

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
      :target: https://github.com/MacHu-GWU/cookiecutter-pygitrepo/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
      :target: https://github.com/MacHu-GWU/cookiecutter-pygitrepo/issues


Cookiecutter PyGitRepo
==============================================================================

``cookiecutter-pygitrepo`` is a `cookiecutter <https://github.com/audreyr/cookiecutter>`_ template for Python / pip installable / AWS Project.

It is to replace my other project template library `pygitrepo <https://github.com/MacHu-GWU/pygitrepo-project>`_.


Features
------------------------------------------------------------------------------

Create and Remove virtualenv::

    # print useful information of your project
    make info

    # create virtualenv
    make up

    # remove virtualenv
    make remove

Install your library and Run Test::

    # run test with pytest
    make test

    # run code coverage test
    make cov

    # run test with multiple python version
    make tox

Automatical Integration with `Travis-CI <https://travis-ci.org/>`_ and `Codecov <https://codecov.io/>`_. Configuration free.

Auto format your source code and test code style into pep8::

    make reformat

Build Document with auto-generated API reference::

    # build sphinx html document site
    make build-doc

    # open your doc in browser
    make view-doc

    # deploy your doc website to s3
    make deploy-doc

Want to publish to `Python Package Index <www.pypi.org>`_ ?, Let's do::

    make publish

Run jupyter nootbook::

    make notebook


**You can easily choose to generate the following tools for your project**.


Python Library Project
------------------------------------------------------------------------------



DevOps Project (Optional, Required if a AWS Project)
------------------------------------------------------------------------------

It provides a Multi Environment config management tools out-of-the-box. It allows you to:

1. define complex derivable config value logic.
2. switch between configs between multiple environments like ``dev | test | prod``.
3. read configs or sensitive data from any where securely. Like json or xml file from your local computer, from remote server, AWS Parameter store, AWS Secret Manager, database. Since it's python, you can do anything.
4. inject configs value to any tools or systems. Like your web application, Terraform, Ansible, VM, Docker, anything.

Magic happens in ``./config`` directory.


AWS Project (Optional)
------------------------------------------------------------------------------




AWS Lambda Project
------------------------------------------------------------------------------

It provides bin tools allows you to easily to:

- package your Lambda Source Code
- build and upload AWS Layer Code



AWS CloudFormation Project
------------------------------------------------------------------------------

It provides frameworks allows you to dynamically construct CloudFormation template and easily deploy it to multi-environment.



AWS Lambda Relative Features
------------------------------------------------------------------------------

It is a AWS Lambda function project? Maybe you want to build a **AWS Lambda Runtime compatible (Linux) deployment package** (require `docker <https://www.docker.com/>`_)::

    make lbd-build-everything

You can **simulate lambda invoke locally with custom event data** like this::

    bash ./bin/lbd/invoke my_func ./lbd-test-event.json

`layers <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`_ can **minimize your build / deploy process to fewer second**. You can build the dependencies once, and deploy it everywhere. Just do::

    make lbd-build-layer
    make lbd-upload-everything
    make lbd-deploy-layer

**Continues deployment is easy**, just do this when it passed the Continues Integration. It use `severless framework <https://serverless.com/>`_ to manage aws infrastructure and configurations::

    make lbd-deploy-all-func


Usage: Generate Project Skeleton
------------------------------------------------------------------------------

.. code-block:: bash

    cd <to-any-dir-for-example-your-github-dir>
    git clone https://github.com/MacHu-GWU/cookiecutter-pygitrepo.git
    python ./cookiecutter-pygitrepo/run_cookiecutter_pygitrepo.py

Note:

    since it use extra_context to inject runtime data such as today's date to the main context, **this won't work properly**::

        cookiecutter https://github.com/MacHu-GWU/cookiecutter-pygitrepo.git


Description
------------------------------------------------------------------------------

notation:

- <tmp>: indicate that this directory / file are temporarily generated, and should not be included in the repo.

::

    <repo_name>
    |-- .github
    |-- .circleci
    |-- bin
        |-- py                  # python environment bin tools and shell scripts
        |-- lbd                 # aws lambda bin tools and shell scripts
        |-- source              # common shell scripts functions
        |-- settings.sh
    |-- build                   # <tmp>
        |-- lambda              # <tmp> for aws lambda function deployment
            |-- source.zip      # <tmp> source code only
            |-- deploy-pkg.zip  # <tmp> source code + dependencies
            |-- layer.zip       # <tmp> dependencies layer
            |-- site-packages   # <tmp> local lambda runtime sandbox, will be used in container
    |-- docs
        |-- build               # <tmp>
            |-- html            # <tmp>
        |-- source
            |-- _static
                |-- css
                |-- js
                |-- .custom-style.rst
                |-- xxx-favicon.ico
                |-- xxx-logo.png
            |-- conf.py
            |-- index.rst
            |-- release-history.rst
        |-- make.bat
        |-- Makefile
    |-- <package_name>
        |-- docs
            |-- __init__.py
        |-- handlers
            |-- __init__.py
            |-- lambda_function1.py
            |-- lambda_function2.py
            |-- ...
        |-- __init__.py
        |-- cli.py
        |-- _version.py
    |-- tests
        |-- all.py              # invoke all test from python script
        |-- test_xxx.py
    |-- .coveragerc
    |-- codecov.yml
    |-- .gitattributes
    |-- .gitignore
    |-- .travis.yml
    |-- AUTHORS.rst
    |-- fix_code_style.py
    |-- LICENSE.txt
    |-- Makefile                # quick access
    |-- MANIFEST.in
    |-- README.rst
    |-- readthedocs.yml
    |-- release-history.rst
    |-- requirements.txt
    |-- requirements-dev.txt
    |-- requirements-doc.txt
    |-- requirements-test.txt
    |-- serverless.yml          # aws lambda configuration
    |-- setup.py
    |-- tox.ini


Dev Guide
------------------------------------------------------------------------------

**To test your change** to ``{{ cookiecutter.repo_name }}``

1. Run ``dev.py``, generate ``learn_awslambda-project`` repo.
2. Test with ``make xxx`` command.



Release Strategy
------------------------------------------------------------------------------

A new version will be released to a release branch every 3 - 6 months.

The master branch represent the latest development version.

All release branches are production ready.

To use specific version, just clone the specific release branch and run ``python ./init_repo.py``
