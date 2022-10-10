#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6
from pisi.actionsapi import get


def setup():
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")
    shelltools.export("LDFLAGS", "%s" % get.LDFLAGS())
    # pisitools.cflags.remove("-lto-wrapper")
    # pisitools.cxxflags.remove("-lto-wrapper")
    # pisitools.cflags.add(" -ffat-lto-objects")
    # pisitools.cxxflags.add(" -ffat-lto-objects")
    qt6.configure()

def build():
    qt6.make()

def install():
    qt6.install()
    
    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt6/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt6/bin/%s" % bin, "/usr/bin/%s-qt6" % bin)

    pisitools.dodoc("LICENSES/*")
