#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("resources.qrc", ".*logo-.*$")
    qt5.configure("clipgrab.pro")

def build():
    qt5.make()
    shelltools.chmod("icon.png", 0644)

def install():
    pisitools.dobin("clipgrab")
    pisitools.insinto("/usr/share/pixmaps/", "icon.png", "clipgrab.png")
    pisitools.dodoc("COPYING", "license.odt") 
