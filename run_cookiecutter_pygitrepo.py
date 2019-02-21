# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
from datetime import datetime, date
from cookiecutter.main import cookiecutter

here = os.path.dirname(__file__)
extra_context = dict(
    _dev_py_ver_major=sys.version_info.major,
    _dev_py_ver_minor=sys.version_info.minor,
    _dev_py_ver_micro=sys.version_info.micro,
    _dev_py_ver_full="{}.{}.{}".format(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro,
    ),
    _current_year=datetime.now().year,
    _current_date=str(date.today()),
)


if __name__ == "__main__":
    sys.stdout.write(here)
    cookiecutter(
        here,
        extra_context=extra_context,
    )
