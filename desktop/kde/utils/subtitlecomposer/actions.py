#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools



def setup():
    # shelltools.export("PKG_CONFIG_PATH", "/usr/lib/ffmpeg4.4/pkgconfig")
    cmaketools.configure("-B build -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DKDE_INSTALL_LIBDIR=lib \
        -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
            -DBUILD_TESTING:BOOL=OFF \
        -DCMAKE_CXX_STANDARD=17 \
        -DQT_MAJOR_VERSION=6 ")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.domo("po/tr.po", "tr", "subtitlecomposer.mo")

    pisitools.dodoc("LICENSES/*", "LICENSE", "README.*")
