{%- set _github_url = 'https://github.com/%(github_username)s/%(repo_name)s'|format(github_username=cookiecutter.github_username, repo_name=cookiecutter.repo_name) -%}
{%- if cookiecutter.doc_service == 'rtd' -%}
{%- set _doc_domain = 'https://%(doc_rtd_project_name)s.readthedocs.io'|format(doc_rtd_project_name=cookiecutter.doc_rtd_project_name) -%}
{%- elif cookiecutter.doc_service == 's3' -%}
{%- set _doc_domain = 'http://%(doc_host_s3_bucket_name)s.s3.amazonaws.com/docs/%(package_name)s/latest'|format(doc_host_s3_bucket_name=cookiecutter.doc_host_s3_bucket_name, package_name=cookiecutter.package_name) -%}
{%- endif -%}
{%- if cookiecutter.doc_service == 'rtd' %}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.doc_rtd_project_name }}/badge/?version=latest
    :target: {{ _doc_domain }}/index.html
    :alt: Documentation Status
{% endif %}
.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}

.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

------

{% if _doc_domain %}
.. image:: https://img.shields.io/badge/Link-Document-blue.svg
      :target: {{ _doc_domain }}/index.html
{% endif %}

{%- if _doc_domain %}
.. image:: https://img.shields.io/badge/Link-API-blue.svg
      :target: {{ _doc_domain }}/py-modindex.html
{% endif %}

{%- if _doc_domain %}
.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
      :target: {{ _doc_domain }}/py-modindex.html
{% endif %}
.. image:: https://img.shields.io/badge/Link-Install-blue.svg
      :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: {{ _github_url }}

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
      :target: {{ _github_url }}/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
      :target: {{ _github_url }}/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.org/pypi/{{ cookiecutter.package_name }}#files


Welcome to ``{{ cookiecutter.package_name }}`` Documentation
==============================================================================

Documentation for ``{{ cookiecutter.package_name }}``.


.. _install:

Install
------------------------------------------------------------------------------

``{{ cookiecutter.package_name }}`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install {{ cookiecutter.package_name }}

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade {{ cookiecutter.package_name }}