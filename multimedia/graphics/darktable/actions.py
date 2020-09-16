#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

def setup():
    pisitools.ldflags.add("-lgs")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DUSE_COLORD=On \
                          -DUSE_OPENJPEG=On \
                          -DUSE_LIBSECRET=On \
                          -DBUILD_USERMANUAL=0 \
                          -DBINARY_PACKAGE_BUILD=1 \
                          -DBUILD_USERMANUAL=False \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_SKIP_BUILD_RPATH=ON \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib \
                          -DCMAKE_INSTALL_LIBEXECDIR=/usr/lib \
                          -DDONT_INSTALL_GCONF_SCHEMAS=1", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()
    

def install():
    shelltools.cd("build")
    cmaketools.install()
    
    # fix libdarktable.so path under /usr/lib
    pisitools.dosym("/usr/lib/darktable/libdarktable.so", "/usr/lib/libdarktable.so")