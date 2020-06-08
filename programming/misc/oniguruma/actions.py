#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "onig-%s" %get.srcVERSION()

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-posix-api \
                         --disable-silent-rules \
                         --disable-static")
    

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())
    
    pisitools.dodoc("COPYING", "README*", "AUTHORS", "ChangeLog")
