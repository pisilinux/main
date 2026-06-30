#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    #shelltools.system("sed -i 's|$(datadir)/pkgconfig|$(libdir)/pkgconfig|g' Makefile.in")
    #shelltools.system("sed -i 's|$(datadir)/pkgconfig|$(libdir)/pkgconfig|g' Makefile.am")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.domove("/usr/share/pkgconfig/iso-codes.pc","/usr/lib/pkgconfig")
    pisitools.removeDir("/usr/share/pkgconfig")

    pisitools.dodoc("TODO*","README.md")
