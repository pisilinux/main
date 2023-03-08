#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DDISABLE_DEPRECATED_QT_FEATURES=ON',
    ' -DQT_PACKAGE_PREFIX=Qt6',
    ' -DJS_PROVIDER=none',
    ' -DWEBVIEW_PROVIDER=none',
    ' -B_build -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build("-C _build")

def install():
	mesontools.install("-C _build")
