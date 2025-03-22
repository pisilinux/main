#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

i = ''.join([
    ' -DCMAKE_BUILD_TYPE=RelWithDebInfo',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -Denable-desktop-manager=OFF',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(i)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("LICENSE", "LGPL-2", "copyright")
