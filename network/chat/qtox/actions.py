#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

i = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DDESKTOP_NOTIFICATIONS=ON',
    ' -D{SPELL,UPDATE}_CHECK=ON',
    ' -DGIT_DESCRIBE{,_EXACT}=v1.18.2'
    ' -DGIT_VERSION=ac1a16ec0bb7ef1f9bbd494a076e661b05937d08'
    ' -Bbuild -G Ninja -L '
    ])

def setup():
	cmaketools.configure(i)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("LICENSE")
