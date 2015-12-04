#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    
    shelltools.export("PYTHON", "/usr/bin/python3.4")
    pythonmodules.compile(pyVer="3.4")

def install():
    shelltools.export("PYTHON", "/usr/bin/python3.4")
    pythonmodules.install(pyVer="3.4")
    
    pisitools.rename("/usr/bin/virtualenv", "virtualenv3")
    
    pisitools.dodoc("LICENSE*", "AUTHORS*", "README*")