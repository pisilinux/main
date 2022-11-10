#!/usr/bin/python

import os, re

#OUR_ID = 42
OUR_ID = 65
OUR_NAME = "gdm"
OUR_DESC = "GDM"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system("useradd -m -d /var/lib/gdm -r -s /bin/false -u %d -g %d %s -c %s" % (OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
        os.system("passwd -ql %s" % (OUR_NAME))

        os.system("/bin/chown gdm:gdm -R /var/lib/gdm")
        os.system("service gdm on")
        os.system("/bin/chown root:gdm -R /var/log/gdm")
    except:
        pass

def postRemove():
    try:
        os.system("userdel %s" % OUR_NAME)
        os.system("groupdel %s" % OUR_NAME)
    except:
        pass
