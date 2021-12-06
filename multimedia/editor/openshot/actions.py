#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    # prevent setup.py from trying to update MIME databases
    shelltools.system("sed -i 's/^ROOT =.*/ROOT = False/' setup.py || die")

    pythonmodules.compile(pyVer="3")

def build():
    pythonmodules.compile(pyVer="3")
    shelltools.system("python3 setup.py build")

def install():
    pythonmodules.install(pyVer="3")

    pisitools.dodoc("COPYING", "README*")
