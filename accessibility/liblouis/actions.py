#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def setup():
 #   autotools.autoreconf("-vfi")
    autotools.configure("--disable-static --enable-ucs4")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog")
    

    shelltools.export("LD_PRELOAD","%s/liblouis/.libs/liblouis.so.12" % get.curDIR())
    shelltools.cd("python")

    pythonmodules.install("--prefix=/usr --optimize=1")
    pythonmodules.install("--prefix=/usr --optimize=1",pyVer = "3")
 
