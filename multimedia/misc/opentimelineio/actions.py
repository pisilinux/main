#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.move("rapidjson-*/*", "src/deps/rapidjson")
    cmaketools.configure("cmake -B build \
                        -DCMAKE_INSTALL_PREFIX=/usr \
                        -DOTIO_FIND_IMATH=ON \
                        -DOTIO_SHARED_LIBS=ON \
                        -DOTIO_CXX_INSTALL=ON \
                        -DOTIO_DEPENDENCIES_INSTALL=OFF")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("LICENSE*", "README*")
