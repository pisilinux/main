#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Dpython=python3")

def build():
    mesontools.build()
    
def install():
    mesontools.install()
    #pisitools.rename("/usr/lib/pkgconfig/pygobject-3.0.pc", "py3gobject-3.0.pc")
    #pisitools.rename("/usr/include/pygobject-3.0/pygobject.h", "py3gobject.h") 
    
    
    pisitools.dodoc("COP*", "NEWS", "README*")
