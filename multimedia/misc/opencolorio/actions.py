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
    #shelltools.system('sed -i "s/-Werror//g" src/core/CMakeLists.txt')
    #shelltools.system('sed -i "s/-Werror//g" src/pyglue/CMakeLists.txt')
    #shelltools.system('sed -i "s/push(hidden)/push(default)/g" src/core/OCIOYaml.cpp')

    # shelltools.makedirs("build")
    # shelltools.cd("build")
    cmaketools.configure("-GNinja \
                          -Bbuild \
                          -DUSE_EXTERNAL_YAML=ON \
                          -DUSE_EXTERNAL_TINYXML=ON \
                          -DPYTHON=python3 \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_SKIP_INSTALL_RPATH=YES \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DOCIO_BUILD_pystring=OFF \
                          -DOCIO_BUILD_STATIC=OFF \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DUSE_EXTERNAL_LCMS=ON")

def build():
    # shelltools.cd("build")
    # cmaketools.make("-j2")
    shelltools.system("ninja -C build")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("README*")
