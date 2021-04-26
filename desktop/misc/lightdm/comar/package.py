#!/usr/bin/python

import os, re

OUR_ID = 620
OUR_NAME = "lightdm"
OUR_DESC = "LightDM"

Cache = "/var/cache/lightdm"
Libdir = "/var/lib/lightdm-data"
Libdir1 = "/var/lib/lightdm"
Logdir = "/var/log/lightdm"


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system ("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system ("useradd -m -d /var/lib/lightdm -r -s /bin/false -u %d -g %d %s -c %s" % (OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))

    except:
        pass
    

    if not os.path.exists(Cache):
       os.makedirs(Cache, mode=0755)

    if not os.path.exists(Libdir):
       os.makedirs(Libdir, mode=0770)
       os.system("chown -R lightdm:lightdm /var/lib/lightdm-data")

    
    if not os.path.exists(Libdir1):
       os.makedirs(Libdir1, mode=0770)
       os.system("chown -R lightdm:lightdm /var/lib/lightdm")
 
    if not os.path.exists(Logdir):
       os.makedirs(Logdir, mode=0711)

    os.system("/bin/chgrp -R lightdm /var/log/lightdm")
    os.system("chmod +t /var/{cache/lightdm,lib/lightdm{,-data}}")

def postRemove():
    try:
        os.system ("userdel %s" % OUR_NAME)
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass 
