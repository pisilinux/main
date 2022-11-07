#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5

def setup():
    shelltools.system("sed -i '/-Werror/d' common-project-config.pri")
    pisitools.dosed("common-project-config.pri", "lib64", "lib")
    qt5.configure()

def build():
    qt5.make("PREFIX=/usr LIBDIR=/usr/lib")

def install():
    qt5.install()

    pisitools.dodoc("COPYING", "README*")
