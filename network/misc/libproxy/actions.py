#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("libproxy/cmake/modules/pacrunner_mozjs.cmk", "mozjs-68", "mozjs-78")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DBIPR=0 \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DPERL_VENDORINSTALL=yes \
                          -DWITH_WEBKIT3:BOOL=ON \
                          -DWITH_VALA=yes \
                          -DCMAKE_CXX_FLAGS='%s' \
                          -DCMAKE_C_FLAGS='%s' \
                          -DWITH_MOZJS:BOOL=ON" % (get.CXXFLAGS(), get.CFLAGS()), sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("README", "ChangeLog", "COPYING")
