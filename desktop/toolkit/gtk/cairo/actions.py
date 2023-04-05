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

def setup():
    pisitools.flags.add("-flto -ffat-lto-objects")

    mesontools.configure("-Dtests=disabled \
                          -Dsymbol-lookup=disabled \
                          -Dspectre=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "README*", "NEWS", "COPYING*")
