#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lxml-%s" % get.srcVERSION()

def build():
    # remove the C extension so that it will be rebuild using the latest Cython
    shelltools.unlink("src/lxml/*.c")
    # fix unused dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()),"doc/*")

    pisitools.dodoc("CHANGES.txt", "LICENSES.txt")