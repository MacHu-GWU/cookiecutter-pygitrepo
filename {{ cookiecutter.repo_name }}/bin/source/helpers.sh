#!/bin/bash
# -*- coding: utf-8 -*-
#
# This script should be sourced to use.


# test if a command is installed in your system
# usage:
#
#   if this_command_exists "brew"; then ...
this_command_exists() {
    if [ -x "$(command -v $1)" ]; then
        return 0
    else
        return 1
    fi
}


# if a file / dir exists, then remove it. do nothing if not exists.
# usage:
#
#   rm_if_exists "~/Documents/GitHub"
rm_if_exists() {
    if [ -e $1 ]; then
        if [ -d $1 ]; then
            rm -r $1
        elif [ -f $1 ]; then
            rm $1
        fi
    fi
}


color_normal="\e[39m"
color_black="\e[30m"
color_red="\e[31m"
color_green="\e[32m"
color_yellow="\e[33m"
color_blue="\e[34m"
color_magenta="\e[35m"
color_cyan="\e[36m"
color_light_gray="\e[37m"
color_dark_gray="\e[90m"
color_light_red="\e[91m"
color_light_green="\e[92m"
color_light_yellow="\e[93m"
color_light_blue="\e[94m"
color_light_magenta="\e[95m"
color_light_cyan="\e[96m"
color_white="\e[97m"


# print a line with color
# usage:
#
#   print_colored_line $color_red "Warning!"
print_colored_line() {
    local TMP_COLOR=$1
    local TMP_TEXT=$2
    printf -- "${TMP_COLOR}${TMP_TEXT}${color_normal}\n"
}
