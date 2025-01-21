#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools

def setup():
    #pisitools.dosed("breeze/breeze.script", "kde.logo.png", "pisi.logo.png")
    #pisitools.dosed("breeze/breeze.script", "Plasma 5.6", "PisiLinux")
    pisitools.dosed("breeze-text/breeze-text.plymouth.cmake", "Plasma @PROJECT_VERSION@", "PisiLinux")
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("LICENSES/*", "README*")
