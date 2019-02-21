# -*- coding: utf-8 -*-

"""
Package Description.
"""


from ._version import __version__

__short_description__ = "Package short description."
__license__ = "MIT"
{% if cookiecutter.author_name -%}
__author__ = "{{ cookiecutter.author_name }}"
{% endif -%}
{% if cookiecutter.author_email -%}
__author_email__ = "{{ cookiecutter.author_email }}"
{% endif -%}
__github_username__ = "{{ cookiecutter.github_username }}"
