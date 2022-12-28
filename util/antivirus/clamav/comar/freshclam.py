# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "ClamAV database updater service"})

@synchronized
def start():
    startService(command="/usr/bin/freshclam",
                 args="-d -p /run/freshclam.pid",
                 pidfile="/run/freshclam.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/freshclam",
                donotify=True)

def status():
    return isServiceRunning("/run/freshclam.pid")
