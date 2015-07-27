#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    pisitools.ldflags.add("-Wl,-rpath,/usr/lib")
    cmaketools.configure("-DBUILD_TESTING=OFF \
                          -DLIB_INSTALL_DIR=lib \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DSYSCONF_INSTALL_DIR=/etc \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIBEXEC_INSTALL_DIR=libexec \
                          -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                          -DPYTHON_EXECUTABLE=/usr/bin/python \
                          -DQT_PLUGIN_INSTALL_DIR=lib/qt5/plugins \
                          -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt5/mkspecs/modules ")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("COPYING")
