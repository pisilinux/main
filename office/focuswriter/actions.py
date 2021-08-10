#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5

def setup():
    #shelltools.system("qmake-qt5  focuswriter.pro")
    qt5.configure("focuswriter.pro")

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("CREDITS", "ChangeLog", "COPYING", "README")
