#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_DIR=/usr',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DENABLE_THUMBNAILER=ON',
    ' -DENABLE_GIO=ON',
    ' -DENABLE_TESTS=OFF',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "COPYING")
