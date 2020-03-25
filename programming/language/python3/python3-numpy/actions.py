#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "numpy-%s" % get.srcVERSION()

shelltools.export("ATLAS", "None")
shelltools.export("PTATLAS", "None")
# fix unused direct dependency analysis
shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.dodoc("LICENSE*")
    
    for dirs in ["doc"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)