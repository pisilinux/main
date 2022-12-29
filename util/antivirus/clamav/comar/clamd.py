# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Clam Anti-Virus Daemon",
                 "tr": "Clam Antivirüs Servisi"})

@synchronized
def start():
    startService(command="/usr/sbin/clamd",
                 pidfile="/run/clamd.pid",
                 donotify=False)
    time.sleep(4)

@synchronized
def stop():
    stopService(command="/usr/sbin/clamd",
                donotify=True)

def status():
    return isServiceRunning("/run/clamd.pid")
