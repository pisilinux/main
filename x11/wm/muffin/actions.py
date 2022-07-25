#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file https://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("--prefix=/usr \
                          --sysconfdir=/etc \
                          --libexecdir=/usr/lib/muffin \
                          --localstatedir=/var")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "README*", "NEWS")
