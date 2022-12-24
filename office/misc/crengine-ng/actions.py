#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

i = ''.join([
    ' -DBUILD_TOOLS=ON',
    ' -DENABLE_LTO=ON',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCRE_BUILD_STATIC=OFF',
    ' -DADD_DEBUG_EXTRA_OPTS=OFF',
    ' -B_build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(i)

def build():
	mesontools.build("-C _build")

def install():
	mesontools.install("-C _build")

	pisitools.dodoc("AUTHORS", "ChangeLog")
