from comar.service import *
import os

serviceType = "script"
serviceDefault = "on"
serviceDesc = _({"en": "VirtualBox",
                 "tr": "VirtualBox"})
serviceConf = "virtualbox"


@synchronized
def start():
        os.system("/sbin/modprobe vboxguest")
        os.system("/sbin/modprobe vboxvideo") 
        os.system("/sbin/modprobe vboxsf")
        os.system("/sbin/modprobe vboxdrv")
        os.system("/sbin/modprobe VBoxService -f ")

