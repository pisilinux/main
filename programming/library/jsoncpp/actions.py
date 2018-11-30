#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DJSONCPP_WITH_CMAKE_PACKAGE=ON \
                          -DBUILD_SHARED_LIBS=ON \
                          -DBUILD_STATIC_LIBS=OFF \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "LICENSE", "README*")
