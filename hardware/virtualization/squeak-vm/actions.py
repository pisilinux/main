#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-int-to-pointer-cast -Wno-int-conversion -Wno-implicit-int -Wno-shift-count-overflow -Wno-implicit-function-declaration -Wno-pointer-to-int-cast -Wno-unused-result -Wno-incompatible-pointer-types -Wno-aggressive-loop-optimizations")
    shelltools.system("./unix/cmake/configure --prefix=/usr --without-quartz --with-x --enable-mpg-mmx")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("unix/doc")
    pisitools.dodoc("COPYING", "LICENSE*", "README*")