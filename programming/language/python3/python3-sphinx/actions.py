#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "Sphinx-%s" % get.srcVERSION()

def build():
    shelltools.system('sed -i "s:sphinx-apidoc:&3:g" setup.py')
    shelltools.system('sed -i "s:sphinx-autogen:&3:g" setup.py')
    shelltools.system('sed -i "s:sphinx-build:&3:g" setup.py')
    shelltools.system('sed -i "s:sphinx-quickstart:&3:g" setup.py')
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    
    pisitools.dodoc("CHANGES", "EXAMPLES")

