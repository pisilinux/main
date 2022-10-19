#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def setup():
    # shelltools.system("sed -i 's/120/600/' test/meson.build")
    options = " --buildtype=release -Dloongson-mmi=disabled \
                          --prefix=/usr \
                          --libdir=lib \
                          -Dvmx=disabled \
                          -Darm-simd=disabled \
                          -Dneon=disabled \
                          -Diwmmxt=disabled \
                          -Dmips-dspr2=disabled \
                          -Dgtk=disabled"

    if get.buildTYPE() == "_emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " --libdir=lib32 \
                   "

    mesontools.configure(options)

def build():
    mesontools.build()

# def check():
    # mesontools.build("test")

def install():
    mesontools.install()

    if get.buildTYPE() == "_emul32":
        return

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README")
