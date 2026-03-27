#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools

def setup():
    kde6.configure("-DBUILD_TESTING=OFF \
                    -DBUILD_KRITA_QT_DESIGNER_PLUGINS=ON \
                    -DKDE_INSTALL_LIBDIR=lib \
                    -DBUILD_TESTING=OFF \
                    -DBUILD_WITH_QT6=ON \
                    -DALLOW_UNSTABLE=QT6 \
                    -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    kde6.make()

def install():
    kde6.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README.md", "LICENSES/*")
