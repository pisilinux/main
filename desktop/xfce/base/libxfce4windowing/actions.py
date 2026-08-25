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

def setup():
    # shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    # autotools.autoreconf("-fiv")
    mesontools.configure("-Dx11=enabled \
                         -Dwayland=enabled \
                         -Dvala=enabled \
                         -Dgtk-doc=true")


    # pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "NEWS", "README*")
