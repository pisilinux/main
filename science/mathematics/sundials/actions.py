#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DKLU_ENABLE=ON \
                          -DMPI_ENABLE=ON \
                          -DOPENMP_ENABLE=ON \
                          -DPTHREAD_ENABLE=ON \
                          -DF77_INTERFACE_ENABLE=ON \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DKLU_LIBRARY_DIR=/usr/lib \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_C_FLAGS='-fPIC -fcommon' \
                          -DEXAMPLES_INSTALL_PATH=/usr/share/sundials/examples", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")

    pisitools.dodoc("LICENSE", "NOTICE", "README*")