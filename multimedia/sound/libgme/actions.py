#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	shelltools.system("mkdir build_")
	shelltools.cd("build_")

	shelltools.system("cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=lib")

def build():
	shelltools.cd("build_")
	cmaketools.make()

def install():
	shelltools.cd("build_")
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())
	
	shelltools.cd("..")
	pisitools.dodoc("changes.txt", "design.txt", "gme.txt", "license*", "readme.txt")

