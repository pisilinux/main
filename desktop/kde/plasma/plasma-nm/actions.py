#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    kde5.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DLIB_INSTALL_DIR=lib \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                    -DBUILD_TESTING=OFF")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("README", "COPYING.LIB", "COPYING")
