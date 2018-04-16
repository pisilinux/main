#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release -DCMAKE_VERBOSE_MAKEFILE=ON --DCMAKE_BUILD_TYPE=Debug -DCMAKE_INSTALL_PREFIX=/usr ..")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("LICENCE", "README.md")
