#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "-DCMAKE_INSTALL_PREFIX=/usr \
                     -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                     -DCMAKE_INSTALL_DATADIR=/usr/share \
                     -DCMAKE_BUILD_TYPE=Release \
                   "

    if get.buildTYPE() == "_emul32":
        shelltools.export("ASFLAGS", "--32")
        shelltools.export("CFLAGS", "-m32")
        shelltools.export("CXXFLAGS", "-m32")
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " -DCMAKE_INSTALL_LIBDIR=lib32 \
                          "

    cmaketools.configure(options, sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("LICENSE.md", "README*")
