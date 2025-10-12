#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools

i = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DBUILD_TESTING=OFF',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -DHWY_SYSTEM_GTEST=ON',
    ' -B build -L '
    ])

def setup():
	cmaketools.configure(i)

def build():
	cmaketools.make("-C build")

def install():
	cmaketools.install("-C build")
