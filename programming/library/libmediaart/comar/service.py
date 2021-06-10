
from comar.service import *

serviceType = "local"
serviceConf = "libmediaart"
serviceDefault = "conditional"

serviceDesc = _({"en": "Libmediaart",
                 "tr": "Libmediaart"})

@synchronized
def start():
    startService(command="/usr/sbin/libmediaart",
                 args = config.get("args", "destroy"),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/libmediaart",
                donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/coffee/ready")):
        start()

def status():
    return checkDaemon("/var/run/libmediaart.pid")

