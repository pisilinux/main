#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DLIB_INSTALL_DIR=lib \
                    -DSYSCONF_INSTALL_DIR=/etc \
                    -DQML_INSTALL_DIR=/usr/lib/qt5/qml \
                    -DPLUGIN_INSTALL_DIR=/usr/lib/qt5/plugins \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                    -DBUILD_TESTING=FALSE \
                    -DKDEPIM_NO_TEXTTOSPEECH=TRUE")

def build():
    kde5.make("VERBOSE=1")

def install():
    kde5.install()

    pisitools.dodoc("COPYING", "COPYING.LIB")
