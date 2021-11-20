# -*- coding: utf-8 -*-

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"

python "${dir_here}/pygitrepo_md5.py" "${dir_here}/pygitrepo.py"
python "${dir_here}/pygitrepo_print.py" "{FORE_GREEN}Hello World"
python "${dir_here}/pygitrepo_os.py"
