#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build") 
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DHDF5_BUILD_HL_LIB=ON \
                          -DHDF5_BUILD_CPP_LIB=ON \
                          -DHDF5_BUILD_FORTRAN=ON", sourceDir="..")
    
    shelltools.cd("..")
    autotools.configure("--prefix=/usr \
                         --enable-cxx \
                         --enable-hl \
                         --enable-threadsafe \
                         --enable-fortran \
                         --enable-build-mode=production \
                         --enable-linux-lfs \
                         --enable-unsupported \
                         --disable-static \
                         --disable-parallel \
                         --disable-sharedlib-rpath \
                         --disable-dependency-tracking \
                         --docdir=/usr/share/doc/hdf5/ \
                         --with-pthread=/usr/lib/ \
                         --with-pic")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/usr/lib/pkgconfig", "build/CMakeFiles/*.pc")
    pisitools.dodoc("ACKNOWLEDGMENTS", "COPYING", "README*", "release_docs/HISTORY-*", "release_docs/RELEASE.txt")
