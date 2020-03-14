#!/bin/bash

# Initialize Config

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/py/python-env.sh

print_colored_line ${color_light_cyan} "run config initialization script ..."
${bin_python} -c "import ${package_name}.devops.config_init"
print_colored_line ${color_green} "complete"
