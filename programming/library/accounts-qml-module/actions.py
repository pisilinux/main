#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt6, autotools, get

def setup():
    # qt6.configure()
    shelltools.system("mkdir build")
    shelltools.cd("build")
    shelltools.system("qmake6-qt6 ../accounts-qml-module.pro PREFIX=/usr")

def build():
    # qt6.make()
    shelltools.cd("build")
    # shelltools.system("qmake6-qt6 make")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    # qt6.install()
    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README*")
