#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools

def setup():
    
    options = "-Denable-docs=false"
    
    
    if get.buildTYPE() == "emul32":
        options += " --libdir=lib32 --bindir=bin32 --libexecdir=libexec32"
        
        
    mesontools.configure(options)

def build():
	
    mesontools.build()

def install():
    mesontools.install()

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/libexec32")
        pisitools.removeDir("/usr/bin32")
        return
    
    pisitools.dodoc("README*", "NEWS", "LICENSE")
