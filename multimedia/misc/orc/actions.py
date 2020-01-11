#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "--prefix=/usr \
              "
    
    if get.buildTYPE() == "emul32":
        options += "--bindir=/usr/emul32 \
                    --libdir=lib32"
                    
    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/emul32")
        return
