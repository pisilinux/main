# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType="server"
serviceDesc=_({"en": "Session Manager",
               "tr": "Oturum Yöneticisi"})
serviceDefault="on"
PIDFILE="/run/elogind.pid"
DAEMON="/usr/lib/elogind/elogind"

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
