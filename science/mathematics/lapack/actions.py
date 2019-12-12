#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("INSTALL/make.inc.gfortran", "-O2 -frecursive", "")
    pisitools.dosed("INSTALL/make.inc.gfortran", "-O0 -frecursive", "")
    '''
    shelltools.copy("INSTALL/make.inc.gfortran", "make.inc")
    if get.ARCH() == "x86_64":
        pisitools.dosed("make.inc", "-O2", "%s -fPIC -m64 -funroll-all-loops" % get.CFLAGS())
        pisitools.dosed("make.inc", "NOOPT    =", "NOOPT    =-m64 -fPIC ")
    else:
        pisitools.dosed("make.inc", "-O2", "%s -fPIC -funroll-all-loops" % get.CFLAGS())
    '''

    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "-DCMAKE_INSTALL_LIBDIR=lib \
               -DBUILD_SHARED_LIBS=ON \
               -DCBLAS=ON \
               -DBUILD_TESTING=OFF"

    if get.buildTYPE() == "static":
        options = "-DCMAKE_INSTALL_LIBDIR=lib \
                   -DBUILD_SHARED_LIBS=OFF \
                   -DCBLAS=ON \
                   -DBUILD_TESTING=OFF"

    cmaketools.configure(options, sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../")
    pisitools.dodoc("LICENSE", "README.md")
