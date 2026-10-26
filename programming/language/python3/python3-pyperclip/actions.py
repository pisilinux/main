#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    python3modules.compile()
    # shelltools.system("python3 setup.py build")

def install():
    python3modules.install()
    pisitools.dodoc("LICENSE*", "README*")
