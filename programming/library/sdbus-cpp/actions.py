#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release "
                          "-DBUILD_SHARED_LIBS=ON "
                          "-DSDBUSCPP_BUILD_CODEGEN=ON "
                          "-DSDBUSCPP_BUILD_TESTS=OFF "
                          "-DSDBUSCPP_BUILD_DOCS=OFF "
                          "-DSDBUSCPP_BUILD_LIBSYSTEMD=OFF "
                          "-DSDBUSCPP_SDBUS_LIB=elogind")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("README.md", "COPYING*", "ChangeLog*")
