#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("--prefix=/usr \
                          --sysconfdir=/etc \
                          --libexecdir=/usr/lib/cinnamon-desktop \
                          --localstatedir=/var \
                          --buildtype=plain")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README*")
