# -*- coding: utf-8 -*-

from pygitrepo import pgr


def print_all(grep=None):
    for key in dir(pgr):
        if not key.startswith("_"):
            value = getattr(pgr, key)
            if grep:
                if grep.lower() in key.lower():
                    print("{} = '{}'".format(key, value))
            else:
                print("{} = '{}'".format(key, value))


print_all("bin")
# print(pgr.PACKAGE_VERSION)
