#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

def setup():
    pisitools.dosed("vokoscreen.pro", "lrelease-qt5", "lrelease")
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("AUTHORS", "COPYING",)
