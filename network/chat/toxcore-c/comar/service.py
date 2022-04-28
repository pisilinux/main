#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "Tox DHT bootstrap daemon"})

serviceDefault = "off"

CFGFILE = "/etc/tox-bootstrapd.conf"
PIDDIR = "/var/run/tox-bootstrapd"
PIDFILE = "%s/tox-bootstrapd.pid" % PIDDIR

@synchronized
def start():
    if not os.path.exists(PIDDIR):
        try:
            os.makedirs(PIDDIR)
        except:
            pass

    startService(command="/usr/bin/tox-bootstrapd",
                 args="--config %s" % CFGFILE,
                 donotify=True)

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
