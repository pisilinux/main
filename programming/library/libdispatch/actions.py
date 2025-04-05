#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

j = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON',
    ' -DBUILD_TESTING=OFF',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    shelltools.export("CC", "clang")
    shelltools.export("CXX", "clang++")
    cmaketools.configure(j)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("LICENSE")
