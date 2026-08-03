# -*- coding: utf-8 -*-

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools


def setup():
    cmaketools.configure("-DTOMLPLUSPLUS_BUILD_MODULES=OFF")


def install():
    cmaketools.install()
    
    pisitools.dodoc("LICENSE", "README.md")
    
    pisitools.remove("/usr/include/meson.build")
    pisitools.removeDir("/usr/share/tomlplusplus")
