#!/usr/bin/python
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
    
    options = "-Denable-introspection=true"
    mesontools.configure(options)

def build():
	
    mesontools.build()

def install():
	
	mesontools.install()
	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")
