#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    #shelltools.makedirs("build")
    #shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DLIB_INSTALL_DIR=lib \
                          -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                          -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README.md", "COPYING.LIB", "ISSUES")
