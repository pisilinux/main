#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6
from pisi.actionsapi import get

#WorkDir="qt-creator-opensource-src-%s" % get.srcVERSION()
def setup():
    # pisitools.dosed("qtcreator.pri", "libexec/qtcreator", "lib/qtcreator")
    # pisitools.dosed("src/tools/tools.pro", "libexec", "lib")
    cmaketools.configure("-B build -G Ninja -DCMAKE_INSTALL_PREFIX=/usr \
                            -DCMAKE_INSTALL_LIBEXECDIR=lib \
                            -DWITH_DOCS=ON \
                            -DBUILD_DEVELOPER_DOCS=ON \
                            -DBUILD_QBS=OFF \
                            -DQTC_CLANG_BUILDMODE_MATCH=ON \
                            -DCLANGTOOLING_LINK_CLANG_DYLIB=ON")

def build():
    qt6.make()

def install():
    qt6.install()

    pisitools.dodoc("LICENSES/*")
