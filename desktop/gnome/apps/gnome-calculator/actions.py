#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get, mesontools, pisitools

def setup():
    mesontools.configure("--libexecdir=/usr/lib")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING*", "NEWS")
