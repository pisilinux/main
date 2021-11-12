#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.cflags.add("-fcommon -fno-plt")
    shelltools.export("CXXFLAGS", "-fno-plt")
    pisitools.ldflags.add("-z,now")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--enable-glamor")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("COPYING", "README*")
