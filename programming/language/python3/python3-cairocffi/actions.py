#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    pythonmodules.compile(pyVer="3")
    shelltools.system("python3 setup.py build")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.dodoc("LICENSE*", "README*")
