#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools, shelltools

def setup():
	mesontools.configure("-Darchive=enabled")

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "NEWS")
	pisitools.dosym("/usr/share/doc/geeqie/NEWS", "/usr/share/doc/geeqie/ChangeLog")
