#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

NoStrip = ["/"]
shelltools.export("CFLAGS", get.CFLAGS())
shelltools.export("LDFLAGS", get.LDFLAGS())

def setup():
	autotools.rawConfigure("--prefix=/usr")

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

