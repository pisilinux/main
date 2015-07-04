#!/usr/bin/python

import os, re
import shutil

OUR_ID = 65
OUR_NAME = "sddm"
OUR_DESC = "sddm"

DATADIR = "/var/lib/sddm"
DATADIRMODE = 0755

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    # On first install...
    if not os.path.exists(DATADIR):
        os.makedirs(DATADIR, DATADIRMODE)

    try:
        os.system ("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system ("useradd -m -d /var/lib/sddm -r -s /bin/false -u %d -g %d %s -c %s" % (OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
        os.system ("passwd -l sddm > /dev/null")
        os.system("/bin/chown -R sddm:sddm %s" % DATADIR)
    except:
        pass

# os.system ("groupadd --system %s" % (OUR_NAME))
# os.system ("useradd -c 'sddm' --system -d /var/lib/sddm -s /sbin/nologin -g %s %s" % (OUR_NAME, OUR_DESC))
    


    # os.system("/bin/chown -R sddm:sddm /var/log/sddm.log")

        

def postRemove():
    try:
        os.system ("userdel %s" % OUR_NAME)
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass





