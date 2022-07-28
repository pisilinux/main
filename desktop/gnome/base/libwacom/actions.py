#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Dudev-dir=/lib/udev \
                          --buildtype=release \
                          -Dtests=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dosym("/usr/lib/libwacom.so.9.0.0", "/usr/lib/libwacom.so.2")

    pisitools.dodoc("COPYING*", "NEWS", "README*")

