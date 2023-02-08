#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools, pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_CXX_COMPILER=g++',
    ' -DENABLE_CLI=ON',
    ' -DENABLE_QT=ON',
    ' -DENABLE_GTK=ON',
    ' -DENABLE_DAEMON=ON',
    ' -DUSE_QT_VERSION=6',
    ' -DQt_DIR=/usr/lib/cmake/Qt6',
    ' -DINSTALL_LIB=OFF',
    ' -DENABLE_TESTS=ON',
    ' -DRUN_CLANG_TIDY=OFF',
    ' -B_build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C _build")

def install():
	mesontools.install("-C _build")
