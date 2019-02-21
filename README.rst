Cookiecutter PyGitRepo
==============================================================================


``cookiecutter-pygitrepo`` is a `cookiecutter <https://github.com/audreyr/cookiecutter>`_ template for

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

Install your library and Run Test:

    # run test with pytest
    make test

    # run code coverage test
    make cov

    # run test with multiple python version
    make tox

Automatical Integration with `Travis-CI <https://travis-ci.org/>`_ and `Codecov <https://codecov.io/>`_. Configuration free.

Build Document with auto-generated API reference:

    # build sphinx html document site
    make build-doc

    # open your doc in browser
    make view-doc

    # deploy your doc website to s3
    make deploy-doc

Want to publish to `Python Package Index <www.pypi.org>`_ ?, Let's do:

    make publish

Run jupyter nootbook:

    make notebook

It is a AWS Lambda function project? Maybe you want to build a AWS Lambda Runtime compatible deployment package (require `docker <https://www.docker.com/>`_).

    make lbd-build-and-upload-deploy-pkg

Usage:

.. code-block:: bash

    cd <to-any-dir>
    git clone https://github.com/MacHu-GWU/cookiecutter-pygitrepo.git
    python ./cookiecutter-pygitrepo/run_cookiecutter_pygitrepo.py

Note:

    since it use extra_context to inject runtime data such as today's date to the main context, this won't work properly::

        cookiecutter https://github.com/MacHu-GWU/cookiecutter-pygitrepo.git
