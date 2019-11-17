#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

NoStrip = "/"

WorkDir = "SmokinGuns-%s" % get.srcVERSION()
shelltools.export("HOME", get.workDIR())
ARCH =("x86_64")
buildDir = "build/release-linux-%s" % ARCH
dataDir = "/usr/share/smokinguns"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def build():
    autotools.make("DEFAULT_BASEDIR=%s copyfiles" % dataDir)

def install():
    pisitools.insinto("/usr/share/smokinguns", "%s/smokinguns.%s" % (buildDir, ARCH), "smokinguns.x86_64")
    pisitools.insinto("/usr/share/smokinguns", "%s/smokinguns_dedicated.%s" % (buildDir, ARCH), "smokinguns_dedicated.x86_64")
    pisitools.dodoc("BUGS", "ChangeLog", "TODO", "README", "*.txt")
    
    shelltools.cd("Smokin' Guns 1.1")
    for dir in ["baseq3", "smokinguns"]:
        fixperms(dir)
        pisitools.insinto(dataDir, dir)
	
	pisitools.dodoc("*.txt")
    
