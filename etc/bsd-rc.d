#!/bin/sh

# PROVIDE: __NAME__
# REQUIRE: DAEMON postgresql nginx
# BEFORE:  LOGIN
# KEYWORD:

. /etc/rc.subr

name=__NAME__
command="__PDIR__/bin/rundjango"

load_rc_config $name
: ${__NAME___enable:=no}
run_rc_command "$1"
