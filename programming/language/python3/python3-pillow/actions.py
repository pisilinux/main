#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

#WorkDir="Imaging-%s" % get.srcVERSION()

def build():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-sign-compare -Wno-pointer-sign")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile(pyVer="3")
    
    # build documentation
    shelltools.export("PYTHONPATH", "%s/Pillow-%s/build/lib.linux-x86_64-cpython-311" % (get.workDIR(), get.srcVERSION()))
    autotools.make("-C docs html")

def install():
    pythonmodules.install(pyVer="3")
    # install header files
    pisitools.insinto("/usr/include/python3.11/Imaging/", "src/libImaging/*.h")
    # install documentation
    pisitools.dohtml("docs/_build/html/*")
    
    
    # 2020-04-08 ToDo
    # * After Qt5 version bump, extract qt5 bindings(python3-pillow-qt5)
