#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

i = ''.join([
    ' --prefix=/usr',
    ' --buildtype=release',
    ' -Dintrospection=enabled',
    ' -Dsystemdsystemunitdir=no',
    ' -Didevice=enabled',
    ' -Dpolkit=enabled '
    ])

def setup():
    mesontools.configure(i)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS")
