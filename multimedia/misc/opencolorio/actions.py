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

    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DUSE_EXTERNAL_YAML=ON \
                          -DUSE_EXTERNAL_TINYXML=ON \
                          -DPYTHON=python3 \
                          -DOCIO_BUILD_pystring=OFF \
                          -DOCIO_BUILD_STATIC=OFF \
                          -DUSE_EXTERNAL_LCMS=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("README*")
