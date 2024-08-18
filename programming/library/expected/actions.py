#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

l = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCATCH_ENABLE_WERROR=ON',
    ' -DEXPECTED_BUILD_PACKAGE_DEB=OFF '
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(l)

def build():
    mesontools.build()

def check():
    mesontools.build("test")

def install():
    mesontools.install()

    pisitools.dodoc("COPYING")
