#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DBUILD_TESTING=OFF \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING*", "TODO")