#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "SDL3_ttf-%s" % get.srcVERSION()

def setup():
    options = "-D CMAKE_INSTALL_PREFIX=/usr"

    if get.buildTYPE() == "emul32":
        #options += " --prefix=/emul32 \
        options += " -DCMAKE_INSTALL_LIBDIR=/usr/lib32 "

        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    cmaketools.configure(options)

def build():
    #pisitools.dosed("Makefile", "-lz -lbz2", "")

    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES.txt", "LICENSE.txt", "README.*")
