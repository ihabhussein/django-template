#!/bin/sh

# PROVIDE: __NAME__
# REQUIRE: DAEMON postgresql nginx
# BEFORE:  LOGIN
# KEYWORD:

. /etc/rc.subr

name=__NAME__
command="__PDIR__/.local/bin/gunicorn -c python:settings_gunicorn project.wsgi:application"
export PYTHONPATH="__PDIR__/src:__PDIR__"
export PYTHONUSERBASE="__PDIR__/.local"
export DJANGO_SETTINGS_MODULE="settings_django"

load_rc_config $name
: ${__NAME___enable:=no}
run_rc_command "$1"
