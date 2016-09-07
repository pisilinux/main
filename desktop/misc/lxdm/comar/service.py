# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType="server"
serviceDesc=_({"en": "lxdm Server",
               "tr": "lxdm Sunucusu"})
serviceDefault="on"
PIDFILE="/run/lxdm.pid"
DAEMON="/usr/sbin/lxdm"

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
