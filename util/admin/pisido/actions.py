#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

def setup():    
    qt5.configure()

def build():
    pisitools.dosed("pisido.pro", "-lqscintilla2", "-lqt5scintilla2")
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("LICENSE", "LISANS", "OKUBUNU", "README")
