#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    pisitools.cflags.add(" -fno-semantic-interposition")
    pisitools.ldflags.add(" -Wl,-Bsymbolic-functions ")
    mesontools.configure("-Dsystemd=false \
                          -Dextensions_tool=true \
                          -Dextensions_app=true \
                          -Dman=true \
                          -Dnetworkmanager=true")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "HACKING.md", "NEWS", "README.md")
