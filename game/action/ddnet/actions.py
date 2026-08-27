#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "DDNet-%s" % get.srcVERSION()

def setup():

    cmaketools.configure(
        "-G Ninja "
        "-DCMAKE_BUILD_TYPE=Release "
        "-DAUTOUPDATE=OFF "
        "-DPREFER_BUNDLED_LIBS=OFF"
    )

def build():
    shelltools.system("ninja")

def install():
    shelltools.system("DESTDIR={} ninja install".format(get.installDIR()))
    
    pisitools.dodoc("license.txt", "README.md")
