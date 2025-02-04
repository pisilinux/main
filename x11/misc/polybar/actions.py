#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

k = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DPYTHON_EXECUTABLE=/usr/bin/python3',
    ' -DBUILD_DOC_HTML=OFF',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(k)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("LICENSE")
