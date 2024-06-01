#!/usr/bin/python
#-*- coding: UTF-8 -*-

from comar.service import *
import os

serviceType = "server"
serviceDesc = _({
    "en": "GNOME Desktop",
    "tr": "GNOME Masaüstü",
})
serviceDefault="on"
PIDFILE="/run/gdm/gdm.pid"
DAEMON="/usr/sbin/gdm"

@synchronized
def start():
    startService(command=DAEMON,
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def status():
    return isServiceRunning(PIDFILE)
