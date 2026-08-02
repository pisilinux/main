# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "libvirt virtualization API daemon",
                 "tr": "libvirt sanallaştırma hizmeti"})
serviceDefault = "on"

DAEMONS = [
    ("/usr/sbin/virtqemud",     "/run/libvirt/virtqemud.pid"),
    ("/usr/sbin/virtnetworkd",  "/run/libvirt/virtnetworkd.pid"),
    ("/usr/sbin/virtnodedevd",  "/run/libvirt/virtnodedevd.pid"),
    ("/usr/sbin/virtstoraged",  "/run/libvirt/virtstoraged.pid"),
    ("/usr/sbin/virtlogd",      "/run/libvirt/virtlogd.pid"),
    ("/usr/sbin/virtnwfilterd", "/run/libvirt/virtnwfilterd.pid"),
    ("/usr/sbin/virtsecretd",   "/run/libvirt/virtsecretd.pid"),
    ("/usr/sbin/virtinterfaced","/run/libvirt/virtinterfaced.pid"),
]

@synchronized
def start():
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin"
    if not os.path.isdir("/run/libvirt"):
        os.makedirs("/run/libvirt", 0755)
    else:
        os.chmod("/run/libvirt", 0755)
    for daemon, pidfile in DAEMONS:
        if isServiceRunning(pidfile=pidfile, command=daemon):
            continue
        if os.path.exists(pidfile):
            os.unlink(pidfile)
        startService(command=daemon,
                     args="--timeout 0 --pid-file %s" % pidfile,
                     detach=True,
                     donotify=True)

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
            try:
                os.kill(int(open(pidfile, "r").read().strip()), 1)
            except (IOError, OSError, ValueError):
                pass

def status():
    for daemon, pidfile in DAEMONS:
        if not isServiceRunning(pidfile=pidfile, command=daemon):
            return False
    return True
