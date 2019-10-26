#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	shelltools.system("mkdir -p build")
	shelltools.cd("build")
	shelltools.system("meson .. \
		              --prefix=/usr \
		              --buildtype=release \
		              -Ddefault_library=shared \
		              ")

def build():
	shelltools.cd("build")
	shelltools.system("ninja")

def install():
	shelltools.cd("build")
	shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
	shelltools.cd("..")
	pisitools.dodoc("COPYING", "README.md", "NEWS")

