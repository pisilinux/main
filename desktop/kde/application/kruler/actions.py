#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DBUILD_TESTING=OFF \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                    -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt5/mkspecs/modules")

def build():
    kde5.make()

def install():
    kde5.install()