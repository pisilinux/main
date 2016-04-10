#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from grp import getgrnam


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.isdir("/run/bumblebee"): os.makedirs("/run/bumblebee", int("0775", 8))
    try:
        os.chown("/run/bumblebee", -1, getgrnam("bumblebee").gr_gid)
    except KeyError:
        os.system("groupadd -r bumblebee")
        os.chown("/run/bumblebee", -1, getgrnam("bumblebee").gr_gid)
        for u in getgrnam("users").gr_mem:
            os.system("gpasswd -a %s bumblebee" % u)
