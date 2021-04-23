#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("")
    shelltools.system("cmake -B build -DCMAKE_INSTALL_PREFIX=/usr -DQML_BOX2D_LIBRARY=/usr/lib/qt/qml/Box2D.2.0")

def build():
    shelltools.system("make -C build")

def install():
    shelltools.system("make -C build DESTDIR=%s" % get.installDIR() + " install")

