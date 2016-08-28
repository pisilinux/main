#!/usr/bin/python

import os, re

OUR_NAME = "docker"
OUR_DESC = "docker"

logfile = "/var/log/docker.log"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system("/usr/sbin/groupadd %s" % OUR_NAME)
        os.system("usermod -a -G docker %s" % os.getusername())
        os.system("/bin/touch %s" % logfile)
        os.system("/bin/chown root:docker %s" % logfile)
        os.system("chmod 0644 %s" % logfile)
    except:
        pass

def preRemove():
    try:
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass