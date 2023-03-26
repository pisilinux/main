#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DENABLE_LAPACK=yes',
    ' -B_build -G Ninja -L '
    ])

def setup():
    #shelltools.unlink("CMakeModules/FindZLIB.cmake")
    cmaketools.configure(j)

def build():
    mesontools.build("-C _build")

def install():
    mesontools.install("-C _build")

    pisitools.dodoc("authors.txt", "Changes.txt")
