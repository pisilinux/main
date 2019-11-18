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

# we get sources from the release zipfile

WorkDir = "darkplaces"
datadir = "/usr/share/quake1"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def setup():	
    pisitools.dosed("makefile.inc", "pardusCC", get.CC())
    pisitools.dosed("makefile.inc", "pardusCFLAGS", "%s -fno-strict-aliasing -ffast-math -funroll-loops " % get.CFLAGS())
    pisitools.dosed("makefile.inc", "pardusLDFLAGS", "%s -lm" % get.LDFLAGS())
    
    for d in ["Docs", "data"]:
        fixperms(d)

def build():
    
    for f in ["cl-nexuiz", "sdl-nexuiz", "sv-nexuiz"]:
        autotools.make("%s DP_FS_BASEDIR=/usr/share/quake1" % f)

def install():
    for f in ["nexuiz-glx", "nexuiz-sdl", "nexuiz-dedicated"]:
        pisitools.dobin("%s" % f)
        
	pisitools.dodir(datadir)
	shelltools.copytree("Nexuiz/data", "%s/%s/nexuiz" % (get.installDIR(), datadir))

    pisitools.dodoc("Nexuiz/Docs/*.txt", destDir="nexuiz")
    pisitools.dohtml("Nexuiz/Docs/*", destDir="nexuiz")

    pisitools.dosym("nexuiz-sdl", "/usr/bin/nexuiz")

