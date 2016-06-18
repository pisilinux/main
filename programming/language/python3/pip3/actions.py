#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="pip-%s" % get.srcVERSION()

def setup():
    pythonmodules.compile(pyVer = "3")
    
def install(): 
    pythonmodules.install(pyVer = "3")
    pisitools.rename("/usr/bin/pip", "pip3")
    
    shelltools.system("sed -i 's|#!/usr/bin/env python$|#!/usr/bin/env python3|' %s/usr/lib/python3.*/site-packages/pip/__init__.py" % get.installDIR())
    shelltools.system("python3 -m compileall %s/usr/lib/python3.*/site-packages/pip/__init__.py" % get.installDIR())
    
