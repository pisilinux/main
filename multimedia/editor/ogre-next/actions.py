#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("cmake .. -DUSE_INTERNAL_TINYXML=OFF \
                          -DINSTALL_LIBENCFS=ON \
                          -DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -G Ninja")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README*")
