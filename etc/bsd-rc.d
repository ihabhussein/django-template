#!/bin/sh

# PROVIDE: __NAME__
# REQUIRE: DAEMON postgresql nginx
# BEFORE:  LOGIN
# KEYWORD:

. /etc/rc.subr

name=__NAME__
command="gunicorn3 -c __CONF__/__SAFE___gunicorn project.wsgi:application"
export PYTHONPATH="__CONF__:__PDIR__/src"
export PYTHONUSERBASE="__PDIR__/.local"
export DJANGO_SETTINGS_MODULE="__SAFE___django"

load_rc_config $name
: ${__NAME___enable:=no}
run_rc_command "$1"
