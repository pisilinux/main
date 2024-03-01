#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools

def setup():
    #shelltools.system("rm -rf po/id")
    kde6.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -DCMAKE_DISABLE_FIND_PACKAGE_PackageKitQt6=ON \
                    -DBUILD_TESTING=OFF")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("LICENSES/*")
