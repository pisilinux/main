#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    kde5.configure("-DBUILD_TESTING=OFF \
                    -DBUILD_KRITA_QT_DESIGNER_PLUGINS=ON \
                    -DKDE_INSTALL_LIBDIR=lib \
                    -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    kde5.make()

def install():
    kde5.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README.md", "LICENSES/*")
