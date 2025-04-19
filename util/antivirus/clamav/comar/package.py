# -*- coding: utf-8 -*-
#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system("/usr/sbin/useradd -r -k /dev/null -m -b /var/lib -U clamav")
    except:
        pass

def postRemove():
    try:
        os.system("/usr/sbin/userdel -r clamav")
        os.system("/usr/sbin/groupdel clamav")
    except:
        pass
