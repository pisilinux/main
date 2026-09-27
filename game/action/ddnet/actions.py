#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "DDNet-%s" % get.srcVERSION()

def setup():
    shelltools.system(
        "cmake -B build -G Ninja "
        "-DCMAKE_INSTALL_PREFIX=/usr "
        "-DCMAKE_BUILD_TYPE=Release "
        "-DAUTOUPDATE=OFF "
        "-DPREFER_BUNDLED_LIBS=OFF"
    )

def build():
    shelltools.system("cmake --build build")

def install():
    shelltools.system("DESTDIR=%s cmake --install build" % get.installDIR())
    
    pisitools.dodoc("license.txt", "README.md")
