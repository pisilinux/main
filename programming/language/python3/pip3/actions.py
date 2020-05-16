#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="pip-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer = "3")
    
def install(): 
    pythonmodules.install(pyVer = "3")
    pisitools.rename("/usr/bin/pip", "pip3")
    pisitools.dodoc("LICENSE*")
    
    # 2020-05-16 Blue DeviL Note:
    # Build documentation
    
    #shelltools.system("sed -i 's|#!/usr/bin/env python$|#!/usr/bin/env python3|' %s/usr/lib/python3.*/site-packages/pip/__init__.py" % get.installDIR())
    #shelltools.system("python3 -m compileall %s/usr/lib/python3.*/site-packages/pip/__init__.py" % get.installDIR())