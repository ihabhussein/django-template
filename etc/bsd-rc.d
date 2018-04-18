#!/bin/sh

# PROVIDE: __NAME__
# REQUIRE: DAEMON postgresql nginx
# BEFORE:  LOGIN
# KEYWORD:

. /etc/rc.subr

name=__NAME__
command="export $(grep -v '^#' "__PDIR__/.env" | xargs) && __PDIR__/.local/bin/gunicorn project.wsgi:application"

load_rc_config $name
: ${__NAME___enable:=no}
run_rc_command "$1"
