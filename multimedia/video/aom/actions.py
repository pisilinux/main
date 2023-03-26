#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools, get

WorkDir="libaom-%s" % get.srcVERSION()

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DBUILD_SHARED_LIBS=1',
    ' -DENABLE_TESTS=0',
    ' -S . -B build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C build")

def install():
	mesontools.install("-C build")

	pisitools.insinto("/usr/share/pixmaps", "aomedia_logo_200.png", "aom.png")
	pisitools.dodoc("AUTHORS", "CHANGELOG", "README.md")
