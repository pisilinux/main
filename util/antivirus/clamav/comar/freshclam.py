# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceConf = "freshclam"
serviceDesc = _({"en": "ClamAV database updater service"})

PIDFILE = "/var/run/freshclam.pid"

@synchronized
def start():
    startService(command="/usr/bin/freshclam",
                 args="--config-file=/etc/clamav/freshclam.conf %s" % config.get("CLIOPTS"),
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/freshclam",
                pidfile=PIDFILE,
                donotify=True)
    if os.path.isfile(PIDFILE): os.unlink(PIDFILE)

def status():
    return isServiceRunning(PIDFILE)
