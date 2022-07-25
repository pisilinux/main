#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("--prefix=/usr \
                          --libexecdir=/usr/lib/cinnamon-settings-daemon \
                          --buildtype=plain")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
