#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CXXFLAGS())
    #autotools.autoreconf("-vfi")
    #autotools.configure()
    
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib \
                          -DBUILD_SHARED_LIBS=ON")

def build():
    cmaketools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    #pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("LICENSE.*")
