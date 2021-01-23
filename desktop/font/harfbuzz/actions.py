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
    options = "-D graphite=enabled \
               -D docs=disabled \
              "

    if get.buildTYPE() == "emul32":
        options += " -D graphite=disabled \
                     -D introspection=disabled \
                   "
                    
    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()
    if get.buildTYPE() == "_emul32":
        return

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
