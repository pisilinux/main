#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "glaze-8.0.0"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-Dglaze_BUILD_EXAMPLES=OFF -DBUILD_TESTING=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()

    shelltools.cd("..")
    pisitools.dodoc("LICENSE*", "README*")
