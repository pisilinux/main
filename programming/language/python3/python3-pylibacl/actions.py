#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    # suppress compiler warnings
    shelltools.export("CFLAGS", "-Wno-strict-aliasing %s" % get.CFLAGS())
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")