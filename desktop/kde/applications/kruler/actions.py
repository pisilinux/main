#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6

def setup():
    kde6.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DBUILD_TESTING=OFF \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                    -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt6/mkspecs/modules")

def build():
    kde6.make()

def install():
    kde6.install()
