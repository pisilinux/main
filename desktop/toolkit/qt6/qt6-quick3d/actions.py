#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6
from pisi.actionsapi import get, cmaketools


def setup():
    # shelltools.export("CC", "clang")
    # shelltools.export("CXX", "clang++")
    # cmaketools.configure("-B build \
                          # -D-DCMAKE_MESSAGE_LOG_LEVEL=STATUS \
                          # -DCMAKE_BUILD_TYPE=Release")

    qt6.configure()

def build():
    # cmaketools.make("-C build")
    # shelltools.system("cmake --build build")
    qt6.make()

def install():
    # shelltools.cd("build")
    # cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    qt6.install()
    
    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt6/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt6/bin/%s" % bin, "/usr/bin/%s-qt6" % bin)

    pisitools.dodoc("LICENSES/*")
