#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "lxml-%s" % get.srcVERSION()

def setup():
    # Setting LC_CTYPE to workaround encoding issue
    shelltools.export("LC_CTYPE", "en_US.UTF-8")

def build():
    # fix unused dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()),"doc/*")

    pisitools.dodoc("CHANGE*", "LICENSE*")