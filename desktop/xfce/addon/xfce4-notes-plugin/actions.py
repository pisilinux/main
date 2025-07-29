#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

i = "-Wno-incompatible-pointer-types -Wno-implicit-function-declaration -Wno-deprecated-declarations"

def setup():
    pisitools.cflags.add(i)
    mesontools.configure("--libexecdir=/usr/lib \
                         --localstatedir=/var \
                         -Ddebug=false")

    # pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")

