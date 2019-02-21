#!/bin/bash
# -*- coding: utf-8 -*-

# Variables from this script:
#
# - DETECTED_OS: Windows | Darwin | Linux
# - OS_IS_WINDOWS: Y | N
# - OS_IS_DARWIN: Y | N
# - OS_IS_LINUX: Y | N
# - OPEN_COMMAND: start in windows, open in Darwin or Linux


if [ "${OS}" = "Windows_NT" ]
then
    DETECTED_OS="Windows"
else
    DETECTED_OS=$(uname -s)
fi

if [ "${DETECTED_OS}" = "Windows" ]
then
    OS_IS_WINDOWS="Y"
    OS_IS_DARWIN="N"
    OS_IS_LINUX="N"
    OPEN_COMMAND="start"
elif [ "${DETECTED_OS}" = "Darwin" ]
then
    OS_IS_WINDOWS="N"
    OS_IS_DARWIN="Y"
    OS_IS_LINUX="N"
    OPEN_COMMAND="open"
elif [ "${DETECTED_OS}" = "Linux" ]
then
    OS_IS_WINDOWS="N"
    OS_IS_DARWIN="N"
    OS_IS_LINUX="Y"
    OPEN_COMMAND="open"
else
    OS_IS_WINDOWS="N"
    OS_IS_DARWIN="N"
    OS_IS_LINUX="N"
    OPEN_COMMAND="unknown_open_command"
fi
