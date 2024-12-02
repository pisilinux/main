#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DONEAPI_INSTALL_ENVDIR=/usr/share/vpl',
    ' -DONEAPI_INSTALL_MODFILEDIR=/usr/share/vpl/modulefiles',
    ' -DBUILD_TOOLS_ONEVPL_EXPERIMENTAL=OFF',
    ' -DBUILD_DISPATCHER_ONEVPL_EXPERIMENTAL=OFF',
    ' -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc',
    ' -DBUILD_TESTS=ON',
    ' -DBUILD_TOOLS=ON',
    ' -DBUILD_DEV=ON',
    ' -B_build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C _build")

def install():
	mesontools.install("-C _build")

	pisitools.dodoc("CHANGELOG.md", "CONTRIBUTING.md")
