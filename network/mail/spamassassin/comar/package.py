#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("sa-update")
    os.system("/bin/chmod 755 /var/lib/spamd")
    os.system("/bin/chown spamd: /var/lib/spamd -R")
