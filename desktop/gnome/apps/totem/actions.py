#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools, get, mesontools, pisitools

def setup():
    mesontools.configure("--libexecdir=/usr/lib \
                          -Denable-gtk-doc=true \
                          -Dwith-plugins=all \
                          -Denable-python=yes")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README*", "NEWS")
