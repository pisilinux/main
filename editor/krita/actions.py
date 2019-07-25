#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5
from pisi.actionsapi import get

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DKDE_INSTALL_LIBDIR=lib \
                    -DBUILD_TESTING=OFF \
                    -DBUILD_UNMAINTAINED=ON")

def build():
    kde5.make()

def install():
    kde5.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README.md", "AUTHORS")
