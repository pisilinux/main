 # -*- coding: utf-8 -*-

from pisi.version import Version

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/update-mime-database /usr/share/mime")


