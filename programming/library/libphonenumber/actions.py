#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs("cpp/build")
    shelltools.cd("cpp/build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_SHARED_LIBS=ON \
                          -DBUILD_STATIC_LIBS=OFF \
                          -DCMAKE_INSTALL_PREFIX=/usr", sourceDir="..")

def build():
    shelltools.cd("cpp/build")
    cmaketools.make()


def install():
    shelltools.cd("cpp/build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    shelltools.cd("../..")
    pisitools.dodoc("LICENSE")
