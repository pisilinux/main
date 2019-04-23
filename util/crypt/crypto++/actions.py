#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

    

def build():
    pisitools.flags.add("-DNDEBUG -fPIC")
    pisitools.dosed("cryptopp.pc", "@VERSION@", get.srcVERSION())
    
    cmaketools.make("dynamic cryptest.exe")
    
    
def install():
    cmaketools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/lib/libcryptopp.a")

    pisitools.insinto("/usr/lib/pkgconfig", "cryptopp.pc")
