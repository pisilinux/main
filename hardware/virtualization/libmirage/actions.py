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

    cmaketools.configure("-DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -DCMAKE_INSTALL_LIBDIR='lib' \
        -DBUILD_SHARED_LIBS=ON \
        -DPOST_INSTALL_HOOKS=OFF \
        -DBUILD_STATIC_LIBS=OFF", sourceDir="..")

def build():
    cmaketools.make("-B build")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # pisitools.dodoc("COPYING", "README")

