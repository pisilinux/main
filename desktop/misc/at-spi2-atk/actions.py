#!/usr/bin/python
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
    options = "--prefix=/usr --sysconfdir=/etc \
              "
                     
    if get.buildTYPE() == "emul32":
        options += " --libdir=lib32"
                
    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()
    if get.buildTYPE() == "emul32":
        return
    
    pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS")
