# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("sources/pyside2")
    shelltools.makedirs("build2")
    shelltools.cd("build2")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_TESTS=OFF \
                          -DPYTHON_EXECUTABLE=/usr/bin/python3", sourceDir="..")


def build():
    shelltools.cd("sources/pyside2/build2")
    cmaketools.make()


def install():
    shelltools.cd("sources/pyside2/build2")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
