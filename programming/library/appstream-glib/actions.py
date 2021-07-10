#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("--prefix=/usr \
                          -Dstemmer=false \
                          -Drpm=false \
                          -Dpisi=true")
    
def build():
    mesontools.build()
    
def install():
    mesontools.install()

    pisitools.dodoc("README*", "NEWS", "COPYING", "AUTHORS")
