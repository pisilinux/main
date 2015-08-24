#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt5/mkspecs/modules \
                          -DQT_PLUGIN_INSTALL_DIR=lib/qt5/plugins \
                          -DLIB_INSTALL_DIR=lib \
                          -DSYSCONF_INSTALL_DIR=/etc \
                          -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DPYTHON_EXECUTABLE=/usr/bin/python3 \
                          -DQML_INSTALL_DIR=/usr/lib/qt5/qml \
                          -DBUILD_TESTING=OFF")

def build():
    kde5.make()

def install():
    kde5.install()    
    
    pisitools.dodoc("COPYING.LIB", "AUTHORS")
