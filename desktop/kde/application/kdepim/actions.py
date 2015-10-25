#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

#WorkDir = "kdepim-15.08.2/kaddressbook"

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DBUILD_TESTING=OFF \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                    -DLIBEXEC_INSTALL_DIR=lib")

def build():
    kde5.make()

def install():
    kde5.install()
    
    pisitools.dodoc("COPYING", "COPYING.LIB")
