# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Cgroup Management Daemon",
                 "tr": "Cgroup Yönetim Servisi"})

serviceDefault="on"

CGMANAGER_PIDFILE = "/run/cgmanager.pid"
CGPROXY_PIDFILE = "/run/cgproxy.pid"

@synchronized
def start():
    startService(command="/usr/bin/cgmanager",
                args="--daemon --mount=subsystems",
                donotify=True)
    
    
    startService(command="/usr/bin/cgproxy",
                args="--daemon",
                donotify=True)

@synchronized
def stop():
    stopService(pidfile=CGPROXY_PIDFILE, donotify=True)
    stopService(pidfile=CGMANAGER_PIDFILE, donotify=True)

def status():
    result = isServiceRunning(CGMANAGER_PIDFILE) and isServiceRunning(CGPROXY_PIDFILE)
    return result
