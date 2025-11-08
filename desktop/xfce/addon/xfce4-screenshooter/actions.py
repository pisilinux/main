#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    # shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    mesontools.configure("-Dwayland=enabled \
                          -Dxfixes=enabled \
                          -Dx11=enabled")



    # pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.insinto("/usr/share/pixmaps/", "icons/scalable/org.xfce.screenshooter.svg")

    pisitools.dodoc("AUTHORS", "COPYING", "README*")

