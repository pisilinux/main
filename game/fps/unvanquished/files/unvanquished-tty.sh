#!/bin/sh
# launcher script for unvanquished tty client

#exec /usr/lib/unvanquished/daemonded -libpath /usr/lib/unvanquished -pakpath /usr/share/unvanquished/pkg -homepath $HOME/.unvanquished
exec /usr/lib/unvanquished/daemon-tty -libpath /usr/lib/unvanquished -pakpath /usr/share/unvanquished/pkg -homepath $HOME/.unvanquished "$@"
