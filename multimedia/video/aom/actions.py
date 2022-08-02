#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="libaom-%s" % get.srcVERSION()

def setup():
    #shelltools.cd("%s" % get.workDIR())
    #shelltools.move("libaom-*", "aom-%s" % get.srcVERSION())
    #shelltools.cd("aom-%s" % get.srcVERSION())
    cmaketools.configure("-S . -B build -G Ninja \
                          -DBUILD_SHARED_LIBS=1 \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DENABLE_TESTS=0")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    #pisitools.dosym("/usr/lib/libaom.so.3.4.0", "/usr/lib/libaom.so.0")

    pisitools.insinto("/usr/share/pixmaps", "aomedia_logo_200.png", "aom.png")

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "CHANGELOG", "README.md")

