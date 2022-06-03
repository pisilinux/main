#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("meson.build", "sendto", deleteLine=True)
    mesontools.configure("-Dgtk_doc=false \
                          -Dintrospection=true \
                          --libexec=/usr/lib")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README.md")
