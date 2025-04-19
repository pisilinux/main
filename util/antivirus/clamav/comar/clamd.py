# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceConf = "clamd"
serviceDesc = _({"en": "Clam Anti-Virus Daemon",
                 "tr": "Clam Antivirüs Servisi"})

PIDFILE = "/var/run/clamd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/clamd",
                 args="--config-file=/etc/clamav/clamd.conf %s" % config.get("CLIOPTS"),
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/clamd",
                pidfile=PIDFILE,
                donotify=True)
    if os.path.isfile(PIDFILE): os.unlink(PIDFILE)

def status():
    return isServiceRunning(PIDFILE)
