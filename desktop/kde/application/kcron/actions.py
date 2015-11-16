#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DLIB_INSTALL_DIR=lib \
                    -DPLUGIN_INSTALL_DIR=/usr/lib/qt5/plugins \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                    -DBUILD_TESTING=OFF")

def build():
    kde5.make()

def install():
    kde5.install()
    
    pisitools.dodoc("README", "TODO", "COPYING", "ChangeLog", "AUTHORS")
