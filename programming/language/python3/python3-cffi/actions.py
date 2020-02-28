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
    pisitools.cflags.add("-Wno-deprecated-declarations")
    # fix unused dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared")
    pythonmodules.compile(pyVer="3")

#def check():
#    pythonmodules.run("-m pytest c/ testing/", pyVer="3")

def install():

    pythonmodules.install(pyVer="3")

    for dirs in ["demo"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)