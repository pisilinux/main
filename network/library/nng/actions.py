#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("Ninja \
                          no-dev \
                          CMAKE_BUILD_TYPE=None \
                          CMAKE_INSTALL_PREFIX=/usr \
                          BUILD_SHARED_LIBS=ON \
                          NNG_ENABLE_TLS=ON \
                          NNG_TLS_ENGINE=wolf \
                          NNG_ENABLE_DOC=OFF \
                          NNG_TESTS=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
