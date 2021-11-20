#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module detects the current operation system.
"""

from __future__ import unicode_literals
import platform


class OSEnum(object):
    windows = "Windows"
    macOS = "Darwin"
    linux = "Linux"
    java = "Java"
    unknown = ""


OS_NAME = platform.system()
IS_WINDOWS = OS_NAME == OSEnum.windows
IS_MACOS = OS_NAME == OSEnum.macOS
IS_LINUX = OS_NAME == OSEnum.linux
IS_JAVA = OS_NAME == OSEnum.java

if OS_NAME not in (OSEnum.windows, OSEnum.macOS, OSEnum.linux):
    raise EnvironmentError("Not supported OS: {}".format(OS_NAME))

if __name__ == "__main__":
    print(OS_NAME)
