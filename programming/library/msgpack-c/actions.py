#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_C_COMPILER=gcc',
    ' -DCMAKE_CXX_COMPILER=g++',
    ' -DMSGPACK_BUILD_EXAMPLES=OFF',
    ' -DMSGPACK_ENABLE_STATIC=OFF',
    ' -B_build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C _build")

def check():
	mesontools.build("-C _build test")

def install():
	mesontools.install("-C _build")
