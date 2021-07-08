#!/usr/bin/python

import os, re
import shutil

OUR_ID = 95
OUR_NAME = "elogind"
OUR_DESC = "elogind"
OUR_GRP ="wheel"

DATADIR = "/var/lib/elogind"
DATADIRMODE = 0755

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    # On first install...
    if not os.path.exists(DATADIR):
        os.makedirs(DATADIR, DATADIRMODE)

    try:
        os.system ("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system ("useradd -m -d /var/lib/elogind -r -s /bin/false -u %d -g %d %s -c %s" % (OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
        os.system ("passwd -l elogind > /dev/null")
        os.system("/bin/chown -R elogind:elogind %s" % DATADIR)
    except:
        pass

def postRemove():
    try:
        os.system ("userdel %s" % OUR_NAME)
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass
