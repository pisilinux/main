#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DBUILD_TESTS=OFF \
                          -DBUILD_WITH_QT4=OFF \
                          -DCMAKE_CXX_STANDARD=14 \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # Docs
    pisitools.dodoc("COPYING","README*")
