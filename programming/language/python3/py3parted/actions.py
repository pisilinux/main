#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pythonmodules

def build():
    shelltools.export("PYTHON", "python3")
    autotools.make()
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    
