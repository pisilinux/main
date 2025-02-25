#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("CMakeLists.txt", "GSettingSchemas", deleteLine=True)
    kde6.configure("-DCMAKE_BUILD_TYPE=Release \
                   -DCMAKE_INSTALL_PREFIX=/usr \
                   -DKDE_INSTALL_LIBDIR=lib \
                   -DINCLUDE_DIR=/include/gtk-3.0/gtk \
                   -DLIBEXEC_INSTALL_DIR=lib \
                   -DSYSCONF_INSTALL_DIR=/etc \
                   -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                   -DBUILD_TESTING=OFF")

def build():
    kde6.make()

def install():
    kde6.install()
