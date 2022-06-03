#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("--libexecdir=/usr/lib")

def build():
    mesontools.build()

def install():
    mesontools.install()
    #these file comes from libhandy
    pisitools.removeDir("/usr/share/locale")
    pisitools.remove("/usr/lib/libhandy-1.so*")
    

    pisitools.dodoc("README.md", "LICENSE*")
