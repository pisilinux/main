#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kde6, qt6
from pisi.actionsapi import get

def setup():
    pisitools.dosed("tools/testapp/main.cpp", "#include <QApplication>", "#include <qt6/QtWidgets/QApplication>")
    shelltools.system("sed -e '/tests/d' -i CMakeLists.txt")
    # shelltools.system("sed -e '/tools/d' -i CMakeLists.txt")
    cmaketools.configure("-B build -DCMAKE_INSTALL_PREFIX=/usr \
                          -DUSE_QT6=ON \
                          -DUSE_QT5=OFF")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS", "README")
