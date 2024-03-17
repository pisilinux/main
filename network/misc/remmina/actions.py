#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=/usr/lib \
        -DWITH_APPINDICATOR=ON \
        -DWITH_NEWS=OFF \
        -DWITH_X2GO=ON \
        -DWITH_GVNC=ON \
        -DCMAKE_INSTALL_PREFIX=/usr", sourceDir="..")

    # pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # pisitools.dodoc("COPYING*", "README.md")
