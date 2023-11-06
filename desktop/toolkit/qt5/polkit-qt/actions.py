#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    cmaketools.configure("-B build5 -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIB_DESTINATION=/usr/lib")

    cmaketools.configure("-B build6 -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DQT_MAJOR_VERSION=6 \
                          -DLIB_DESTINATION=/usr/lib")

def build():
    shelltools.cd("build5")
    cmaketools.make()

    shelltools.cd("../build6")
    cmaketools.make()

def install():
    shelltools.cd("build5")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../build6")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "TODO", "README*")
