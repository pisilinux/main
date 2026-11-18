#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt6
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools



def setup():
    shelltools.system("sed -i 's/CONFIG += c++11/CONFIG += c++17/' qpdfview.pri")

    shelltools.system("/usr/lib/qt6/bin/lrelease qpdfview.pro")
    shelltools.system("qmake6-qt6 qpdfview.pro")

def build():
    # qt6.make()
    autotools.make()

def install():
    # qt6.install()
    shelltools.system("make INSTALL_ROOT=%s install" % get.installDIR())

    pisitools.dodoc("CONTRIBUTORS",  "COPYING", "README")


