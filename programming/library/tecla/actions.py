#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get


libdir = "/usr/lib"

def setup():
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.domove("/usr/share/pkgconfig/*.pc", "%s/pkgconfig" % libdir)
    pisitools.removeDir("/usr/share/pkgconfig")
    
    pisitools.dodoc("LICENSE", "NEWS", "README*")
