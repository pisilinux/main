#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    # suppress compiler warnings
    shelltools.export("CFLAGS", "-Wno-implicit-function-declaration -Wno-unused-but-set-variable -Wno-nonnull %s" % get.CFLAGS())
    # fix unused dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile()
    
    #pythonmodules.run("setup.py build_sphinx")
    
#def check():
#    pythonmodules.compile("test")

def install():
     # suppress compiler warnings
    pisitools.cflags.add("-Wno-implicit-function-declaration")
    pythonmodules.install()