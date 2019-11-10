#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("tar xf ../blue.tar.gz")
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()
    
    pisitools.insinto("/usr/share/wallpapers/pisilinux-blue", "blue/*")

    pisitools.dodoc("COPYING", "AUTHORS")
