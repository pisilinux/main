from comar.service import *
import os

serviceType = "script"
serviceDefault = "on"
serviceDesc = _({"en": "VirtualBox",
                 "tr": "VirtualBox"})
serviceConf = "virtualbox"
PIDFILE = "/run/virtualbox.pid"

@synchronized
def start():
        os.system("/usr/bin/vboxreload")
        #os.system("/sbin/modprobe vboxguest")
        #os.system("/sbin/modprobe vboxvideo") 
        #os.system("/sbin/modprobe vboxsf")
        #os.system("/sbin/modprobe vboxdrv")
        

@synchronized
def reload():
    if os.path.exists(PIDFILE):
        os.kill(int(open(PIDFILE, "r").read().strip()), 1)

@synchronized
def stop():
    stopService(pidfile=PIDFILE, donotify=True)
    if os.path.isfile(PIDFILE): os.unlink(PIDFILE)

def status():
    return isServiceRunning(pidfile=PIDFILE)


