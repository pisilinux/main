#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")    

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_BUILD_TYPE=RelWithDebInfo \
                          -DUSE_QT5=ON \
                          -DDBUS_CONFIG_FILENAME=sddm_org.freedesktop.DisplayManager.conf \
                          -DUSE_WAYLAND=ON \
                          -DCMAKE_INSTALL_LIBEXECDIR=/usr/lib/sddm \
                          -DBUILD_MAN_PAGES=ON", sourceDir=".." )

def build():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.make()

def install():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.install()
    
    pisitools.insinto("/usr/share/sddm/themes/pisi-linux-gray", "../pisi-linux-gray-0.1/*")

    pisitools.dodoc("../LICENSE")
