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
    cmaketools.configure("-B build \
                            -G Ninja \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DCMAKE_BUILD_TYPE=Release \
                            -DEMBREE_ISPC_SUPPORT=ON \
                            -DEMBREE_TUTORIALS=OFF \
                            -DEMBREE_BACKFACE_CULLING=OFF")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    pisitools.dodir("/usr/bin")
    shelltools.move("%s/usr/embree-vars.*" % get.installDIR(), "%s/usr/bin/" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("CHANGELOG.md", "LICENSE.txt", "README*")
