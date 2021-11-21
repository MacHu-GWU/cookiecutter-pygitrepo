#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module empower bash script to print colored text easily.

Usage::

    $ python pygitrepo_print.py "mini_colored_text_template_here"

Mini colored text template is a Python f-string liked format
https://docs.python.org/3/tutorial/inputoutput.html. Some examples are::

    "{FORE_RED}this is Red,{STYLE_RESET_ALL} this is normal, {BACK_GREEN} this is green{STYLE_RESET_ALL}"
"""

from __future__ import print_function, unicode_literals

# ------ colorama source code start ------
# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
'''
This module generates ANSI character codes to printing colors to terminals.
See: http://en.wikipedia.org/wiki/ANSI_escape_code
'''

CSI = '\033['


def code_to_chars(code):
    return CSI + str(code) + 'm'


class AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.
        # Upon instantiation we define instance attributes, which are the same
        # as the class attributes but wrapped with the ANSI escape sequence
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class AnsiFore(AnsiCodes):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    RESET = 39

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX = 90
    LIGHTRED_EX = 91
    LIGHTGREEN_EX = 92
    LIGHTYELLOW_EX = 93
    LIGHTBLUE_EX = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX = 96
    LIGHTWHITE_EX = 97


class AnsiBack(AnsiCodes):
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47
    RESET = 49

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX = 100
    LIGHTRED_EX = 101
    LIGHTGREEN_EX = 102
    LIGHTYELLOW_EX = 103
    LIGHTBLUE_EX = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX = 106
    LIGHTWHITE_EX = 107


class AnsiStyle(AnsiCodes):
    BRIGHT = 1
    DIM = 2
    NORMAL = 22
    RESET_ALL = 0


Fore = AnsiFore()
Back = AnsiBack()
Style = AnsiStyle()
# ------ colorama source code end ------

mapper = dict(
    FORE_BLACK=Fore.BLACK,
    FORE_RED=Fore.RED,
    FORE_GREEN=Fore.GREEN,
    FORE_YELLOW=Fore.YELLOW,
    FORE_BLUE=Fore.BLUE,
    FORE_MAGENTA=Fore.MAGENTA,
    FORE_CYAN=Fore.CYAN,
    FORE_WHITE=Fore.WHITE,
    FORE_RESET=Fore.RESET,
    FORE_LIGHTBLACK_EX=Fore.LIGHTBLACK_EX,
    FORE_LIGHTRED_EX=Fore.LIGHTRED_EX,
    FORE_LIGHTGREEN_EX=Fore.LIGHTGREEN_EX,
    FORE_LIGHTYELLOW_EX=Fore.LIGHTYELLOW_EX,
    FORE_LIGHTBLUE_EX=Fore.LIGHTBLUE_EX,
    FORE_LIGHTMAGENTA_EX=Fore.LIGHTMAGENTA_EX,
    FORE_LIGHTCYAN_EX=Fore.LIGHTCYAN_EX,
    FORE_LIGHTWHITE_EX=Fore.LIGHTWHITE_EX,
    BACK_BLACK=Back.BLACK,
    BACK_RED=Back.RED,
    BACK_GREEN=Back.GREEN,
    BACK_YELLOW=Back.YELLOW,
    BACK_BLUE=Back.BLUE,
    BACK_MAGENTA=Back.MAGENTA,
    BACK_CYAN=Back.CYAN,
    BACK_WHITE=Back.WHITE,
    BACK_RESET=Back.RESET,
    BACK_LIGHTBLACK_EX=Back.LIGHTBLACK_EX,
    BACK_LIGHTRED_EX=Back.LIGHTRED_EX,
    BACK_LIGHTGREEN_EX=Back.LIGHTGREEN_EX,
    BACK_LIGHTYELLOW_EX=Back.LIGHTYELLOW_EX,
    BACK_LIGHTBLUE_EX=Back.LIGHTBLUE_EX,
    BACK_LIGHTMAGENTA_EX=Back.LIGHTMAGENTA_EX,
    BACK_LIGHTCYAN_EX=Back.LIGHTCYAN_EX,
    BACK_LIGHTWHITE_EX=Back.LIGHTWHITE_EX,
    STYLE_BRIGHT=Style.BRIGHT,
    STYLE_DIM=Style.DIM,
    STYLE_NORMAL=Style.NORMAL,
    STYLE_RESET_ALL=Style.RESET_ALL,
)

if __name__ == "__main__":
    import sys

    text = sys.argv[1]

    print((text.format(**mapper) + Style.RESET_ALL))
