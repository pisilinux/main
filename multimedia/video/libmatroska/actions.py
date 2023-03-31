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
    #pisitools.dosed("make/linux/Makefile", "CXXFLAGS=", "CXXFLAGS+=")
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                          -DBUILD_SHARED_LIBS=ON")

def build():
    #shelltools.cd("make/linux")
    #autotools.make("PREFIX=/usr \
                   #LIBEBML_INCLUDE_DIR=/usr/include/ebml \
                   #LIBEBML_LIB_DIR=/usr/lib")
                   
    cmaketools.make()

def install():
    #shelltools.cd("make/linux")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    #pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("README*")
