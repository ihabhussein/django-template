#!/bin/sh

# PROVIDE: __NAME__
# REQUIRE: DAEMON postgresql nginx
# BEFORE:  LOGIN
# KEYWORD:

. /etc/rc.subr

name=__NAME__
command="gunicorn3 project.wsgi:application"
export PYTHONPATH="__CONF__:__PDIR__/src"
export PYTHONUSERBASE="__PDIR__/.local"
export DJANGO_SETTINGS_MODULE="__SAFE___django"
export GUNICORN_CMD_ARGS="-b 127.0.0.1:__PORT__ -w 4 --reload --capture-output --error-logfile /var/log/__NAME__.err --access-logfile /var/log/__NAME__.log"

load_rc_config $name
: ${__NAME___enable:=no}
run_rc_command "$1"
