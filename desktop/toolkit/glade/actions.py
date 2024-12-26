#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("sed -i 's/webkit2gtk-4.0/webkit2gtk-4.1/' meson.build")
    mesontools.configure("--prefix=/usr -Dgtk_doc=true -Dgladeui=true -Dgjs=auto")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README*", "TODO")
