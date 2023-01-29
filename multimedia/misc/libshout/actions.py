#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools

i = ''.join([
    ' --enable-theora',
    ' --enable-speex',
    ' --disable-static '
    ])

def setup():
    autotools.autoreconf("-fi")
    autotools.configure(i)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
