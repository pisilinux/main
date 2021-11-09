#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed('CMakeLists.txt', '"cmake"', '"lib/cmake"')

    shelltools.system("mkdir build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DUSE_SHARED_MBEDTLS_LIBRARY=ON \
                          -DMBEDTLS_FATAL_WARNINGS=OFF \
                          -DINSTALL_MBEDTLS_HEADERS=ON", sourceDir="..")

def build():
    cmaketools.make("-C build")

def install():
    cmaketools.rawInstall("DESTDIR=%s -C build" % get.installDIR())

    pisitools.dodoc("ChangeLog", "LICENSE", "README*")
