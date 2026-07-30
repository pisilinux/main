#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

j = ''.join([
    ' --prefix=/usr',
    ' --enable-release',
    ' --disable-native',
    ' --disable-cups',
    ' --disable-static '
    ])

def setup():
    autotools.configure(j)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "LICENSE", "LICENSE_ADDENDUM")
