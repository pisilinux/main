#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.export("PYTHON", "/usr/bin/python2.7")
    shelltools.system("sed -i 's|#!/usr/bin/env python$|#!/usr/bin/env python2|' virtualenv.py")
    pythonmodules.compile(pyVer="2.7")

def install():    
    shelltools.export("PYTHON", "/usr/bin/python2.7")
    pythonmodules.install(pyVer="2.7")
    
    pisitools.dodoc("LICENSE*", "AUTHORS*", "README*")