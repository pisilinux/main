# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "DNSCrypt-proxy client",
                 "tr": "DNSCrypt-proxy istemcisi"})
serviceDefault = "off"

PIDFILE="/run/dnscrypt-proxy.pid"

@synchronized
def start():
    # path to executable
    # creates a pid file, sets the working directory and calls the jar file
    startService(command="/usr/bin/dnscrypt-proxy-comar-compat.sh",
                 args="",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def ready():
    start()

def status():
    return isServiceRunning(pidfile=PIDFILE)
