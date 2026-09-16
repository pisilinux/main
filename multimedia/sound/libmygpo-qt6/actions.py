#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
        -DMYGPO_BUILD_TESTS=OFF \
        -DBUILD_WITH_QT6=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("LICENSE")
