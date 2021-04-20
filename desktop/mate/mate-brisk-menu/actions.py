#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("--prefix=/usr --libexecdir=/usr/lib")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "LICENSE", "README*")
