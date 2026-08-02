# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({
    "en": "TLP Power Management",
    "tr": "TLP Güç Yönetimi Hizmeti"
})
serviceDefault = "on"

DAEMON = "/usr/sbin/tlp"

@synchronized
def start():
    startService(command=DAEMON,
                 args="init start",
                 donotify=True)

@synchronized
def stop():
    run(f"{DAEMON} init stop")

def status():

    return get_status()
