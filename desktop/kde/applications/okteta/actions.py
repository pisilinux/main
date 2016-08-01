#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib \
                          -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("COPYING*", "ChangeLog", "README*", "TODO")
