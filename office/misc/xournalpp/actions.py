#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, pisitools, get

def setup():
	cmaketools.configure("-B_build -DCMAKE_BUILD_TYPE=Release")

def build():
	cmaketools.make("-C _build")
	cmaketools.make("-C _build translations")

def install():
	cmaketools.install("-C _build install")

	pisitools.dodoc("AUTHORS", "CHANGELOG.md")
