#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools

def setup():
	pass

def build():
	pass

def check():
	autotools.make("-C tests")
	autotools.make("-C tests/threads")

def install():
	for t in shelltools.ls("src/*"):
		pisitools.insinto("/usr/include", "%s" % t)

