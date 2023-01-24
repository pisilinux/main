#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools, pisitools

j = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_BUILD_TYPE=RelWithDebInfo',
    ' -DUSE_SYSTEM_TAGLIB=ON',
    ' -DUSE_SYSTEM_PROJECTM=ON',
    ' -B_build -G Ninja -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    mesontools.build("-C _build")

def install():
    mesontools.install("-C _build")

    pisitools.dodoc("README-TURKISH.md", "README.md")
