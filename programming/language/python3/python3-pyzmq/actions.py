#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    # suppress compiler warnings
    shelltools.export("CFLAGS", "-Wno-implicit-function-declaration -Wno-unused-but-set-variable -Wno-nonnull -Wno-tautological-compare -Wno-deprecated-declarations %s" % get.CFLAGS())
    # fix unused dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    python3modules.compile()
    
    #python3modules.run("setup.py build_sphinx")
    
#def check():
#    python3modules.compile("test")

def install():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-implicit-function-declaration")
    python3modules.install()
