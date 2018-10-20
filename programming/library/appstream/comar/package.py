#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/appstreamcli refresh-cache --force")

def preRemove():
    os.system("/bin/rm -rf /var/cache/app-info")
