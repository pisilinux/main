# -*- coding: utf-8 -*-

import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Clam Anti-Virus Daemon",
                 "tr": "Clam Antivirüs Servisi"})

@synchronized
def start():
    startService(command="/usr/sbin/clamd",
                 #chuid="clamav",
                 pidfile="/run/clamd.pid",
                 donotify=False)
    time.sleep(3)
    startService(command="/usr/bin/freshclam",
                 args="-d -p /run/freshclam.pid",
                 #chuid="clamav",
                 pidfile="/run/freshclam.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/clamd",
                        donotify=True)
    time.sleep(4)
    stopService(command="/usr/bin/freshclam",
                        donotify=True)

def status():
    return isServiceRunning("/run/clamd.pid") and isServiceRunning("/run/freshclam.pid")
