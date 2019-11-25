#!/bin/sh
# launcher script for unvanquished client

#exec /usr/lib/unvanquished/daemonded -libpath /usr/lib/unvanquished -pakpath /usr/share/unvanquished/pkg -homepath $HOME/.unvanquished
exec /usr/lib/unvanquished/daemon -libpath /usr/lib/unvanquished -pakpath /usr/share/unvanquished/pkg -homepath ${HOME}/.unvanquished "$@"
