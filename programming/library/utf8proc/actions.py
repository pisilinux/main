#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools

def setup():
	shelltools.makedirs("_build")
	shelltools.cd("_build")
	cmaketools.configure("-DBUILD_SHARED_LIBS=1", sourceDir = "..")

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	shelltools.cd("_build")
	cmaketools.install()

	pisitools.insinto("/usr/lib/pkgconfig", "../libutf8proc.pc.in", "libutf8proc.pc")
