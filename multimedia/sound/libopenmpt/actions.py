#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

NoStrip = ["/usr/lib"]

def setup():
	autotools.autoreconf("-vfi")
	autotools.configure("--disable-static --without-portaudiocpp")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())

	pisitools.dodoc("LICENSE", "README.md")
