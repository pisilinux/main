# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "libvirt virtualization API daemon",
                 "tr": "libvirt sanallaştırma hizmeti"})
serviceDefault = "on"

DAEMONS = [
    ("/usr/sbin/virtqemud",    "/run/libvirt/virtqemud.pid"),
    ("/usr/sbin/virtnetworkd", "/run/libvirt/virtnetworkd.pid"),
    ("/usr/sbin/virtnodedevd", "/run/libvirt/virtnodedevd.pid"),
    ("/usr/sbin/virtstoraged", "/run/libvirt/virtstoraged.pid"),
]

@synchronized
def start():
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin"
    for daemon, pidfile in DAEMONS:
        if os.path.exists(pidfile):
            os.unlink(pidfile)
        startService(command=daemon,
                     args="--timeout 0 --pid-file %s" % pidfile,
                     detach=True,
                     donotify=True)
    if not os.path.isdir("/run/libvirt"):
        os.makedirs("/run/libvirt", 0755)
    else:
        os.chmod("/run/libvirt", 0755)

@synchronized
def stop():
    for daemon, pidfile in DAEMONS:
        stopService(pidfile=pidfile,
                    command=daemon,
                    donotify=True)
        if os.path.exists(pidfile):
            os.unlink(pidfile)

@synchronized
def reload():
    for daemon, pidfile in DAEMONS:
        if os.path.exists(pidfile):
            os.kill(int(open(pidfile, "r").read().strip()), 1)

def status():
    return isServiceRunning(pidfile="/run/libvirt/virtqemud.pid")
