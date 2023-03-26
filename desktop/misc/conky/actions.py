#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools, pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE="RELEASE"',
    ' -DBUILD_CURL=ON',
    ' -DBUILD_IMLIB2=OFF',
    ' -DBUILD_BUILTIN_CONFIG=OFF',
    ' -B_build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C _build")

def install():
	mesontools.install("-C _build")

	pisitools.doman("conky.1")
	pisitools.insinto("/etc/conky", "data/conky.conf")
