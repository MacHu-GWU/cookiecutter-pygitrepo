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
#   rm_if_exists "~/venvs/python/3.8.11/my_venv"
rm_if_exists() {
    if [ -e $1 ]; then
        if [ -d $1 ]; then
            rm -r $1
        elif [ -f $1 ]; then
            rm $1
        fi
    fi
}


# if a dir not exists, then create it and all necessary parent dir.
# usage:
#
#   mkdir_if_not_exists "~/venvs/python/3.8.11/my_venv"
mkdir_if_not_exists() {
    if ! [ -e $1 ]; then
        mkdir -p $1
    fi
}


# exit if not exists
# usage:
#
#    ensure_not_exists "~/venvs/python/3.8.11/my_venv"
ensure_not_exists() {
    if [ -e $1 ]; then
        echo "${1} already exists!"
        exit 1
    fi
}
