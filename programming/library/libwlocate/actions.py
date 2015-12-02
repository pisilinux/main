#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="libwlocate-code-213bcf6fb073d968af5e849a5c1828603f69e5ac/master"

def build():
    autotools.make("-f Makelib")
    autotools.make()
    
def install():
    pisitools.insinto("/usr/lib", "libwlocate.so")
    pisitools.insinto("/usr/include", "libwlocate.h")
    pisitools.insinto("/usr/bin", "lwtrace")
    
    pisitools.dodoc("COPYING", "README", "CREDITS")