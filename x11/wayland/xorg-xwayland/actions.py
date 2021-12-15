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
    mesontools.configure("-Dipv6=true \
                          -Dxcsecurity=true \
                          -Ddri3=true \
                          -Dxwayland_eglstream=true \
                          -Dglamor=true \
                          -Dxkb_dir=/usr/share/X11/xkb \
                          -Dxkb_output_dir=/var/lib/xkb")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.remove("/usr/lib/xorg/protocol.txt")
    pisitools.remove("/usr/share/man/man1/Xserver.1")
    
    pisitools.dodoc("COPYING", "README*")
