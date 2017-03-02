#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.export("CFLAGS", "-lpthread")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                                        -DENABLE_ASCII_MODE=OFF \
                                        -DENABLE_PACKAGING=OFF \
                                        -DBUILD_CONTRIBS_LIB:BOOL=ON \
                                        -DLIB_DESTINATION:PATH=/usr/lib \
                                        -DLUCENE_SYS_INCLUDES:PATH=/usr/lib \
                                        -DDISABLE_MULTITHREADING=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS","README","COPYING","ChangeLog")
