#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir="Imaging-%s" % get.srcVERSION()

def build():
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # install header files
    pisitools.insinto("/usr/include/python3.8/Imaging/", "src/libImaging/*.h")