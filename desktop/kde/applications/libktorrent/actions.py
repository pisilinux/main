#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("sed -i 's|07|08|g' CMakeLists.txt")
    shelltools.system("sed -i 's|90|0|g' CMakeLists.txt")
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("ChangeLog", "LICENSES/*")
