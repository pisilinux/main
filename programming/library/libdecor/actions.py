#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    options = " -Ddemo=false"


    if get.buildTYPE() == "_emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " -Dgtk=disabled --libdir=lib32"


    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    #shelltools.cd("..")
    pisitools.dodoc("LICENSE", "README*")
