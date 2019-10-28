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
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DUSE_QT5=ON \
                          -DUSE_QT5=ON \
                          -DUSE_LINK_TIME_OPTIMIZATION=ON", sourceDir=".." )

def build():
    shelltools.cd("build")

    cmaketools.make()

def install():
    shelltools.cd("build")

    cmaketools.install()
    
    shelltools.cd("..")

    pisitools.dodoc("README*", "LICENSE")
