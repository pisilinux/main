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
    autotools.autoreconf("-if")
    autotools.configure("\
                         --disable-static \
                         --enable-dri \
                         --enable-viaregtool \
                         --enable-debug \
                         --enable-xv-debug \
                        ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("COPYING", "ChangeLog", "NEWS", "README")
