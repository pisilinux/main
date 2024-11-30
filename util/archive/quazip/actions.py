#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-B build5 -DCMAKE_INSTALL_PREFIX=/usr \
                                    -DQUAZIP_QT_MAJOR_VERSION=5 \
                                    -DBUILD_WITH_QT4:BOOL=OFF")

    cmaketools.configure("-B build6 -DCMAKE_INSTALL_PREFIX=/usr \
                                    -DQUAZIP_QT_MAJOR_VERSION=6 \
                                    -DBUILD_WITH_QT4:BOOL=OFF")

def build():
    cmaketools.make("-C build5")
    cmaketools.make("-C build6")

def install():
    shelltools.cd("build5")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../build6")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README.md", "NEWS.txt")
