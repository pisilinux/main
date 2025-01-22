#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # shelltools.system("sed -i 's|5.11.0|5.90.0|g' CMakeLists.txt")
    kde6.configure("-DBUILD_QT5=OFF")

def build():
    kde6.make()

def install():
    kde6.install()

