#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --without-x \
                         --enable-cxx \
                         --enable-ld-version-script \
                         --with-pic")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.dosym("/usr/lib/libtiff.so.6.0.1", "/usr/lib/libtiff.so.5")
        pisitools.dosym("/usr/lib32/libtiff.so.6.0.1", "/usr/lib32/libtiff.so.5")
        pisitools.dosym("/usr/lib/libtiffxx.so.6.0.1", "/usr/lib/libtiffxx.so.5")
        pisitools.dosym("/usr/lib32/libtiffxx.so.6.0.1", "/usr/lib32/libtiffxx.so.5")
        return

    pisitools.rename("/%s/tiff-%s" % (get.docDIR(), get.srcVERSION()), get.srcNAME())
