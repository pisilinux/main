#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = ''.join([
    ' --enable-udisks',
    ' --disable-static',
    ' --disable-old-actions',
    ' --with-gtk=3 '
    ])

def setup():
    autotools.configure(i)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O2,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "TODO")
