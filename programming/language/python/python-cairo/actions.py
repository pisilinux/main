#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    pythonmodules.compile()
    
    
def install():
    pythonmodules.install()

    pisitools.dodoc("COPYING*", "README*","NEWS*")
