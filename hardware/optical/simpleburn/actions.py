#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():  
    pisitools.dosed("CMakeLists.txt", "doc/\$", "share/doc/$")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DBURNING=LIBBURNIA")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

