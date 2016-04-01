#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("breeze/breeze.script", "kde.logo.png", "pisi.logo.png")
    pisitools.dosed("breeze/breeze.script", "Plasma 5.6", "PisiLinux")
    pisitools.dosed("breeze-text/breeze-text.plymouth.cmake", "Plasma @PROJECT_VERSION@", "PisiLinux")
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING", "README")
