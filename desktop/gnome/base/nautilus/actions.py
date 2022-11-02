#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("-Dselinux=false \
                          -D docs=true \
                          -Dpackagekit=false")

def build():
    mesontools.build

def install():
    mesontools.install()

    pisitools.dosym("/usr/lib/pkgconfig/libnautilus-extension-4.pc", "/usr/lib/pkgconfig/libnautilus-extension.pc")

    pisitools.dodoc("LICENSE", "NEWS", "README*")
