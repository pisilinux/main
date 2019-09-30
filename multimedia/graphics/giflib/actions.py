#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.copytree("../giflib-%s" % (get.srcVERSION().replace("_", "~")), "../giflib-%s-32" % get.srcVERSION())
    #libtools.libtoolize("--force --install")
    #autotools.autoreconf("-fi")
    
    #autotools.configure("--disable-static")

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")
    shelltools.cd("../giflib-%s-32" % get.srcVERSION())
    shelltools.export("CC", "gcc -m32")
    shelltools.export("CXX", "g++ -m32")
    autotools.make("-j1")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    shelltools.cd("../giflib-%s-32" % get.srcVERSION())
    autotools.rawInstall("PREFIX=/usr LIBDIR=/usr/lib32 BINDIR=/usr/emul32 DESTDIR=%s" % get.installDIR())
    
    pisitools.removeDir("/usr/emul32")
    pisitools.remove("/usr/lib/libgif.a")
    pisitools.remove("/usr/lib32/libgif.a")

    pisitools.dohtml("doc/")
    pisitools.dodoc("ChangeLog","NEWS")
