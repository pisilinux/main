#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build") 
    shelltools.system("meson .. --prefix=/usr -Dpython=python3")
    
   
def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    
def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    pisitools.rename("/usr/lib/pkgconfig/pygobject-3.0.pc", "py3gobject-3.0.pc")
    pisitools.rename("/usr/include/pygobject-3.0/pygobject.h", "py3gobject.h") 
    
    
    shelltools.cd("..")
    pisitools.dodoc("COP*", "NEWS", "README*")
