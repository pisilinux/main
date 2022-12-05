#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools

i = ''.join([
    ' --disable-rpath',
    ' --disable-nls',
    ' --disable-static',
    ' PYTHON_VERSION=3',
    ' --enable-python '
    ])

def setup():
    autotools.configure(i)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS")
