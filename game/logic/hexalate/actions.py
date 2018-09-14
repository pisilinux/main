#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    qt5.configure(parameters="PREFIX=/usr")

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("CREDITS", "INSTALL", "ChangeLog", "COPYING", "README")
