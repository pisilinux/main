#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import mesontools, pisitools

def setup():
    pisitools.dosed("meson.build", "webkit2gtk-4.0", "webkit2gtk-4.1")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("NEWS", "README*", "COPYING")
