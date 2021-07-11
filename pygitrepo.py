# -*- coding: utf-8 -*-

"""
This is a drop-in-ready script.
"""

import os
from os.path import (
    basename, join, abspath, dirname, exists, expanduser
)
import platform


def ensure_list(value):
    if value is None:
        return []
    return value


class PyVer(object):
    def __init__(self, version):
        self.version = version

        try:
            self.validate_version(version)
        except:
            error = "'%s' is not a valid Python Version. It should be like ${major}.${minor}.{micro}. For example: '3.6.8'" % version
            raise ValueError(error)

        chunks = version.split(".")
        self.major = int(chunks[0])
        self.minor = int(chunks[1])
        self.micro = int(chunks[2])

    def validate_version(self, version):
        assert version.count(".") == 2
        chunks = version.split(".")
        major = int(chunks[0])
        minor = int(chunks[1])
        micro = int(chunks[2])
        assert major in [2, 3]

    @property
    def major_and_minor(self):
        return "{}.{}".format(self.major, self.minor)


class OS:
    windows = "Windows"
    darwin = "Darwin"
    linux = "Linux"
    java = "Java"


class Project(object):
    def __init__(self,
                 dir_project_root=None,
                 package_name=None,
                 pypi_name=None,
                 rtd_name=None,
                 python_version_for_dev=None,
                 python_versions_to_support=None):
        self.dir_project_root = abspath(dir_project_root)  # type: str
        self.package_name = package_name  # type: str
        self.pypi_name = pypi_name  # type: str
        self.rtd_name = rtd_name  # type: str
        self.python_version_for_dev = python_version_for_dev  # type: PyVer
        self.python_versions_to_support = ensure_list(python_versions_to_support)  # type: list

        self.home = abspath(expanduser("~"))
        self.os = platform.system()
        self.is_windows = self.os == OS.windows
        self.is_mac = self.os == OS.darwin
        self.is_linux = self.os == OS.linux
        self.is_java = self.os == OS.java

    @property
    def git_repo_name(self):
        return basename(self.dir_project_root)

    @property
    def package_name_slugify(self):
        """
        :rtype: str
        """
        return self.package_name.replace("_", "-")

    def _if_none_then_package_name(self, value):
        if value is None:
            return self.package_name
        return value

    @property
    def python_package_index_name(self):
        """
        :rtype: str
        """
        return self._if_none_then_package_name(self.pypi_name)

    @property
    def read_the_doc_name(self):
        """
        :rtype: str
        """
        return self._if_none_then_package_name(self.read_the_doc_name)

    # --- Repo file structure
    @property
    def path_readme(self):
        return join(self.dir_project_root, "README.rst")

    @property
    def dir_sphinx_doc(self):
        return join(self.dir_project_root, "docs")

    @property
    def dir_sphinx_source(self):
        return join(self.dir_sphinx_doc, "source")

    @property
    def dir_sphinx_build(self):
        return join(self.dir_sphinx_doc, "build")

    @property
    def dir_sphinx_build_html(self):
        return join(self.dir_sphinx_build, "html")

    @property
    def dir_sphinx_build_html_index(self):
        """

        :return:
        """
        return join(self.dir_sphinx_build, "index.html")

    """
    path_sphinx_doc_build=${tmp_dir_project_root}/docs/build

    path_sphinx_doc_build_html=${path_sphinx_doc_build}/html
    path_sphinx_index_html=${path_sphinx_doc_build}/html/index.html

    path_sphinx_config=${path_sphinx_doc_source}/conf.py

    path_version_file=${tmp_dir_project_root}/${package_name}/_version.py

    path_requirement_file=${tmp_dir_project_root}/requirements.txt
    path_dev_requirement_file=${tmp_dir_project_root}/requirements-dev.txt
    path_doc_requirement_file=${tmp_dir_project_root}/requirements-doc.txt
    path_test_requirement_file=${tmp_dir_project_root}/requirements-test.txt

    path_test_dir=${tmp_dir_project_root}/tests
    path_coverage_annotate_dir=${tmp_dir_project_root}/.coverage.annotate
    path_tox_dir=${tmp_dir_project_root}/.tox

    path_auto_pep8_script=${tmp_dir_project_root}/fix_code_style.py

    path_build_dir=${tmp_dir_project_root}/build
    path_dist_dir=${tmp_dir_project_root}/dist
    path_egg_dir=${tmp_dir_project_root}/${package_name}.egg-info
    path_pytest_cache_dir=${tmp_dir_project_root}/.pytest_cache
    """

    # --- Virtualenv related path
    @property
    def venv_name(self):
        return "{}_venv".format(self.package_name)

    @property
    def dir_venv(self):
        return join(
            self.home,
            "venvs",
            "python",
            self.python_version_for_dev.major_and_minor,
            self.venv_name,
        )

    @property
    def dir_venv_bin(self):
        if self.is_windows:
            return join(self.dir_venv, "Scripts")
        else:
            return join(self.dir_venv, "bin")

    @property
    def dir_site_packages(self):
        if self.is_windows:
            return join(self.dir_venv, "Lib", "site-packages")
        else:
            return join(self.dir_venv, "lib", self.python_version_for_dev.major_and_minor, "site-packages")

    @property
    def dir_site_packages64(self):
        if self.is_windows:
            return join(self.dir_venv, "Lib64", "site-packages")
        else:
            return join(self.dir_venv, "lib64", self.python_version_for_dev.major_and_minor, "site-packages")

    @property
    def bin_activate(self):
        return join(self.dir_venv_bin, "activate")

    @property
    def bin_python(self):
        return join(self.dir_venv_bin, "python")

    @property
    def bin_pip(self):
        return join(self.dir_venv_bin, "pip")

    @property
    def bin_pytest(self):
        return join(self.dir_venv_bin, "pytest")

    @property
    def bin_twine(self):
        return join(self.dir_venv_bin, "twine")

    @property
    def bin_tox(self):
        return join(self.dir_venv_bin, "tox")

    @property
    def bin_jupyter(self):
        return join(self.dir_venv_bin, "jupyter")

    @property
    def bin_sphinx_quick_start(self):
        return join(self.dir_venv_bin, "sphinx-quickstart")

    @property
    def bin_aws(self):
        return join(self.dir_venv_bin, "aws")

    @property
    def bin_ansible(self):
        return join(self.dir_venv_bin, "ansible")

    #--
    # def is_windows(self):
    #     print(os.)


if __name__ == "__main__":
    dir_project_root = dirname(abspath(__file__))
    package_name = "hello_world"

    project = Project(
        dir_project_root=dir_project_root,
        package_name=package_name,
        python_version_for_dev="3.6.2",
        python_versions_to_support=["3.6.2", "3.7.9"],
    )

    print(project.dir_project_root)
    print(project.home)
