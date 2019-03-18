#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i 's|python2|python2.7|g' {setup.py,virt-convert,virt-clone,virt-install,virt-manager,virt-xml}")
    
    pythonmodules.configure()
    pythonmodules.compile()

def install():
    pythonmodules.install()
    #pisitools.dodoc("COPYING", "NEWS", "README*", "PKG-INFO")
