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
    options = "meson --prefix=/usr -Denable-docs=false \
              "
    
    if get.buildTYPE() == "emul32":
        options += "--libdir=lib32 .."
                
    shelltools.system(options)
    
   
def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    
def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        return
    
    shelltools.cd("..")
    pisitools.dodoc("README*", "NEWS", "LICENSE")
