# -*- coding: utf-8 -*-

from comar.service import *

import os

serviceType = "local"
serviceDesc = _({"en": "FIXME",
                 "tr": "FIXME"})

serviceDefault = "on"

PIDFILE = "/run/bumblebeed.pid"
DAEMON = "/usr/sbin/bumblebeed"

@synchronized
def start():
    os.system("modprobe bbswitch load_state=0 unload_state=1")
    startService(command=DAEMON,
                 args="--daemon",
                 detach=True)

    os.system("pidof -o %PPID " + "%s > %s" % (DAEMON, PIDFILE))

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def status():
    return isServiceRunning(pidfile=PIDFILE)
