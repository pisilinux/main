#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools, get

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=release',
    ' -DCREDITSDIR=/usr/share/doc/rawtherapee',
    ' -DLICENCEDIR=/usr/share/doc/rawtherapee',
    ' -B_build',
    ' -G Ninja -L '
    ])

def setup():
    cmaketools.configure(j, installPrefix='/usr')

def build():
    mesontools.build("-C _build")

def install():
    mesontools.install("-C _build")
