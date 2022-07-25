#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    pisitools.dosed("data/nemo.desktop.in", "Name=Files", "Name=Nemo")
    mesontools.configure("--prefix=/usr \
                          --libexecdir=/usr/lib/nemo \
                          --buildtype=plain")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
