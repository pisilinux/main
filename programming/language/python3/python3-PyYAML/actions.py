#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "PyYAML-%s" % get.srcVERSION()

def build():
    pisitools.cflags.add("-Wno-pointer-sign -Wno-incompatible-pointer-types -Wno-sign-compare -Wno-discarded-qualifiers")
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    pythonmodules.compile(pyVer="3")
    
def check():
    pythonmodules.compile("test", pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")