from comar.service import *
import os

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Docker Management Service",
                 "tr": "Docker Yönetim Hizmeti"})

pidfile = "/var/run/docker.pid"
logfile = "/var/log/docker.log"

@synchronized
def start():
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin"
    os.system("/sbin/modprobe -va bridge nf_nat br_netfilter")

    startService(command="/usr/bin/docker",
                args="daemon -p %s -s overlay --dns 8.8.8.8 --dns 8.8.4.4" % (pidfile),
                detach=True,
                pidfile=pidfile,
                donotify=False)

@synchronized
def stop():
    stopService(command="/usr/bin/docker",
                donotify=False)

def status():
    return isServiceRunning(pidfile)
