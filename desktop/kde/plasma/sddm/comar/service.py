# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType="server"
serviceDesc=_({"en": "sddm Server",
               "tr": "sddm Sunucusu"})
serviceDefault="on"
PIDFILE="/run/sddm/sddm.pid"
DAEMON="/usr/bin/sddm"

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
