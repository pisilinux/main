#!/usr/bin/python

import os, re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system("getent group flatpak || /usr/sbin/groupadd -g 93 flatpak")
        os.system("getent passwd flatpak || /usr/sbin/useradd -g flatpak -u 93 -d /var/empty -s /bin/false -c 'flatpak User' flatpak")
        os.system("/usr/bin/passwd -l flatpak")
    except:
        pass

def preRemove():
    try:
        os.system ("groupdel flatpak")
    except:
        pass