# -*- coding: utf-8 -*-

"""
Create Python Github Repository file skeleton at ``/path-to/cookiecutter-pygitrepo/tmp/{{ cookiecutter.repo_name }}``
"""

from __future__ import print_function, unicode_literals
import json
import shutil
from cookiecutter_pygitrepo.config import Config
from cookiecutter_pygitrepo.helpers import strip_comments

from pathlib_mate import Path
from cookiecutter.main import cookiecutter

dir_here = Path(__file__).absolute().parent

if __name__ == "__main__":
    # read config from cookiecutter-pygitrepo.json
    path_cookiecutter_pygitrepo_json = Path(dir_here, "cookiecutter-pygitrepo.json")
    data = json.loads(
        strip_comments(path_cookiecutter_pygitrepo_json.read_text())
    )
    del data["_please_ignore_this"]
    config = Config(**data)
    config.path_cookiecutter_pygitrepo_json = path_cookiecutter_pygitrepo_json.abspath

    # dump context data to cookiecutter.json
    path_cookiecutter_json = Path(dir_here, "cookiecutter.json")
    path_cookiecutter_json.write_text(json.dumps(config.to_context_data(), indent=4))

    # clean up existing environment
    dir_output = Path(dir_here, "tmp")
    dir_output_project_root = Path(dir_output, config.repo_name)
    if dir_output_project_root.exists():
        shutil.rmtree(dir_output_project_root.abspath)

    # create project skeleton
    cookiecutter(
        template=dir_here.abspath,
        output_dir=dir_output.abspath,
        no_input=True,
    )
