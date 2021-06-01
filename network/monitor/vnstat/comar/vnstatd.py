# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Simple Network traffic monitor Daemon",
                 "tr": "Basit bir ağ trafik görüntüleme Servisi"})
serviceConf = "vnstatd"

pidfile = "/run/vnstatd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/vnstatd",
                 args="-d -p %s " % pidfile,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile, donotify=True)

def status():
    return isServiceRunning(pidfile)
