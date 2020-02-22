#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-stringop-truncation -Wno-deprecated-declarations -Wno-incompatible-pointer-types -Wno-discarded-qualifiers -Wno-sign-conversion -Wno-sign-compare")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    
    for dirs in ["vectors"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)