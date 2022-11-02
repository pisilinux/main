#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools

def setup():
    options = " -Dbrotli=disabled \
                -Dintrospection=enabled"

    #if get.buildTYPE() == "_emul32":
        #options += " --libdir=/usr/lib32 \
                     #--bindir=/usr/bin32 \
                     #--sbindir=/usr/sbin32 \
                     #-Dintrospection=disabled \
                     #-Dtls_check=false"


        #shelltools.export("CC", "%s -m32" % get.CC())
        #shelltools.export("CXX", "%s -m32" % get.CXX())
        #shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    mesontools.configure(options)
    
    

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    mesontools.build

def install():
    mesontools.install()


    if get.buildTYPE() == "_emul32":
        pisitools.removeDir("/usr/bin32")
        pisitools.removeDir("/usr/sbin32")
    pisitools.dodoc("README", "NEWS", "AUTHORS")
