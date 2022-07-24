#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools


def setup():
    options = "-D docs=disabled \
              "

    if get.buildTYPE() == "emul32":
        options += " -D graphite2=disabled \
                     --libdir=/usr/lib32 \
                     --bindir=/usr/bin32 \
                     -D introspection=disabled \
                   "
                   
    else:
        options += "-Dintrospection=enabled \
                    -D graphite2=enabled \
                    -Ddocs=enabled"
                    
    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
