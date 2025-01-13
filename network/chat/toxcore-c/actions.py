#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DMUST_BUILD_TOXAV=ON',
    ' -DEXPERIMENTAL_API=ON',
    ' -DDHT_BOOTSTRAP=OFF',
    ' -DENABLE_STATIC=OFF',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
	cmaketools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.insinto("/etc", "other/bootstrap_daemon/tox-bootstrapd.conf")
	pisitools.dodoc("LICENSE")
