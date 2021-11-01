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

#WorkDir="."

def setup():
    #shelltools.cd("%s" % get.workDIR())
    #shelltools.move("/*", "aom-%s" % get.srcVERSION())
    #shelltools.cd("aom-%s" % get.srcVERSION())
    cmaketools.configure("-S . -B build -G Ninja \
                          -DBUILD_SHARED_LIBS=1 \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DENABLE_TESTS=0", sourceDir="..")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    pisitools.dosym("/usr/lib/libaom.so.3.2.0", "/usr/lib/libaom.so.0")

    shelltools.cd("%s" % get.workDIR())
    pisitools.dodoc("AUTHORS", "CHANGELOG", "README.md")

