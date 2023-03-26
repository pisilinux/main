#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools,  pisitools

j = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DPYTHON_EXECUTABLE=/usr/bin/python3',
    ' -DZ3_USE_LIB_GMP=True',
    ' -DZ3_LINK_TIME_OPTIMIZATION=True',
    ' -DZ3_BUILD_LIBZ3_SHARED=True',
    ' -DZ3_BUILD_PYTHON_BINDINGS=True',
    ' -DZ3_INSTALL_PYTHON_BINDINGS=True',
    ' PYTHON=/usr/bin/python3',
    ' -B_build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C _build")

def install():
	mesontools.install("-C _build")

	pisitools.dodoc("RELEASE_NOTES.md")
