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
    shelltools.system("sed -e 's/cxx_std_14/cxx_std_17/g' -i CMakeLists.txt || die")
    cmaketools.configure("-Bbuild \
        -DGSL_TEST=ON \
        -DCMAKE_CXX_FLAGS='%s' \
        -DCMAKE_EXE_LINKER_FLAGS='%s' \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=Release" % (get.CXXFLAGS(), get.LDFLAGS()))

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("LICENSE", "README*")
