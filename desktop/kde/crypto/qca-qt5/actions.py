#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DBUILD_TESTS=OFF \
                          -DQCA_SUFFIX=qt5 \
                          -DQCA_INSTALL_IN_QT_PREFIX=ON")

def build():
    cmaketools.make()    

def install():   

    cmaketools.install()    

    pisitools.dodoc("README", "TODO", "COPYING")
