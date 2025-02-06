#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, shelltools, pisitools

def setup():
    mesontools.configure("--prefix=/usr --buildtype=release")

def build():
    mesontools.build()

def install():
    shelltools.chmod("include/librist/librist.h", mode = 0644)
    mesontools.install()

    pisitools.dodoc("COPYING", "THANKS.md")
