#!/usr/bin/python
#
# Currently, as in some other LFS based distros, providing an user account for flatpak breaks
# the FUSE and non-sudo installations.
# However, I am leaving this file in the repo just in case.

import os, re

OUR_NAME = "flatpak"
OUR_DESC = "flatpak"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system("groupadd -r %s" % OUR_NAME)
        os.system("useradd -r -g %s -d / -s /bin/false -c %s %s" % (OUR_NAME, OUR_DESC, OUR_NAME))

    except:
        pass

def postRemove():
    try:
        os.system("userdel %s" % OUR_NAME)
        os.system("groupdel %s" % OUR_NAME)
    except:
        pass
