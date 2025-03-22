#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

y = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_BUILD_TYPE=None',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
	cmaketools.configure(y)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("COPYING")
