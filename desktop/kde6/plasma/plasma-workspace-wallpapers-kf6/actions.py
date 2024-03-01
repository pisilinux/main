#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("tar xf ../blue.tar.gz")
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()
    
    pisitools.insinto("/usr/share/wallpapers/pisilinux-blue", "blue/*")
    pisitools.insinto("/usr/share/wallpapers/sweet-cat", "../Sweet-cat/*")
    pisitools.insinto("/usr/share/wallpapers/pisi-crocus-ancyrensis", "../pisi-crocus-ancyrensis/*")

    pisitools.dodoc("COPYING", "AUTHORS")
