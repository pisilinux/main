#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2019 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import qt5
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("src/main.cpp", "/usr/lib/at-spi2-core/at-spi-bus-launcher", "/usr/libexec/at-spi2/at-spi-bus-launcher")
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dodoc("LICENSE", "README.md")
