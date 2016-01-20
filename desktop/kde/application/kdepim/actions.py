#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DBUILD_TESTING=OFF \
                    -DLIB_INSTALL_DIR=lib \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON")
    
def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING", "COPYING.LIB")