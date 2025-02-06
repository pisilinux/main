#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

y = ''.join([
    ' --prefix=/usr',
    ' --buildtype=release',
    ' -D{docs,mans}=true '
    ])

def setup():
    mesontools.configure(y)

def build():
    mesontools.build()

def check():
#    mesontools.build("test") # required X display environment.
    pass

def install():
    mesontools.install()

    pisitools.dodoc("LICENSE")
