#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools

l = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DBUILD_SHARED_LIBS=1',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(l)

def build():
    mesontools.build()

def check():
    pass

def install():
    mesontools.install()
