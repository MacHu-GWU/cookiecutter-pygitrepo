# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.package_name}}'

if not re.match(MODULE_REGEX, module_name):
    msg = ('ERROR: The package name (%s) is not a valid Python package name. '
           'Please do not use a - and use _ instead, valid example: foo_bar' % module_name)

    #Exit to cancel project
    sys.exit(1)

supported_python_versions = '{{ cookiecutter.supported_python_versions }}'
try:
    for version in supported_python_versions.split(" "):
        chunks = version.split(".")
        assert len(chunks) == 3

        for s in chunks:
            int(s)
        assert int(chunks[0]) in [2, 3, 4]
except:
    msg = ('Error: the supported python versions (%s) is invalid, ' 
           'valid example: 2.7.13 3.4.6 3.5.3 3.6.2' % supported_python_versions)
    print(msg)
    sys.exit(1)
