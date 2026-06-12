#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")
    autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr \
                        --sysconfdir=/etc \
                        --localstatedir=/var \
                        --enable-plugins \
                        --enable-clipart \
                        --enable-templates \
                        --enable-introspection")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps/", "abiword.png")
