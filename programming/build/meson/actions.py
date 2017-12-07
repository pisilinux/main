#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    
    pisitools.insinto("/usr/share/vim/vimfiles", "syntax-highlighting/vim/*")
    pisitools.remove("/usr/share/vim/vimfiles/README")
    
    pisitools.dodoc("COPYING", "README*")
