#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://gnu.org/licenses/gpl-3.0.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("-Degl_device=true")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "README*", "NEWS")
