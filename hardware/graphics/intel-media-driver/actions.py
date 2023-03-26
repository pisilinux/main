#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DMEDIA_BUILD_FATAL_WARNINGS=OFF',
    ' -B_build -G Ninja -Wno-dev -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C _build")

def install():
	mesontools.install("-C _build")
