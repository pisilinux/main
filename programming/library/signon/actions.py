#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("sed -i -e 's/qdbusxml2cpp/qdbusxml2cpp-qt5/' src/signond/signond.pro")
    qt5.configure(parameters="PREFIX=/usr LIBDIR=/usr/lib")

def build():
    qt5.make()

def install():
    qt5.install()