#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("cmake .. -DPORT=GTK \
                        -DCMAKE_BUILD_TYPE=Release \
                        -DCMAKE_SKIP_RPATH=ON \
                        -DCMAKE_INSTALL_PREFIX=/usr \
                        -DLIB_INSTALL_DIR=/usr/lib \
                        -DLIBEXEC_INSTALL_DIR=/usr/lib \
                        -DENABLE_GTKDOC=NO \
                        -DPYTHON_EXECUTABLE=/usr/bin/python \
                        -DUSE_LIBHYPHEN=OFF \
                        -G Ninja")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    #autotools.make()

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    #shelltools.cd("..")

    #pisitools.dodoc("LICENSE", "README")
