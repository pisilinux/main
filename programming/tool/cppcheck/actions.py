#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools,  pisitools

j = ''.join([
    ' -DUSE_Z3=ON',
    ' -DUSE_QT6=ON',
    ' -DUSE_BOOST=ON',
    ' -DUSE_THREADS=ON',
    ' -DHAVE_RULES=ON',
    ' -DPYTHON_EXECUTABLE=/usr/bin/python3',
    ' -DBUILD_GUI=ON',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -DBUILD_TESTS=ON',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_CONFIGURATION_TYPES=Release',
    ' -DUSE_BUNDLED_TINYXML2=OFF',
    ' -DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON',
    ' -DENABLE_CHECK_INTERNAL=ON',
    ' -DWITH_QCHART=ON',
    ' -B_build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C _build")

def check():
	pass

def install():
	mesontools.install("-C _build")

	pisitools.dodoc("AUTHORS")
