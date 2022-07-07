#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

Libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"
bindir = "/usr/bin32" if get.buildTYPE() == "emul32" else "/usr/bin"

def setup():
    options = "-Ddocumentation=false \
               --libdir=%s \
               --bindir=%s \
              " % (Libdir, bindir)

    if get.buildTYPE() == "emul32":
        options += " -Ddocumentation=false \
                   "
    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "bin32", "bin")
            pisitools.insinto("/usr/share/pixmaps/icons", "doc/publican/sources/images/wayland.png")
        return

    pisitools.dodoc("COPYING", "CONTRIBUTING*", "README")
