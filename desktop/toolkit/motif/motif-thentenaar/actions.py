#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = ''.join([
    ' --prefix=/usr',
    ' --sysconfdir=/etc',
    ' --libdir=/usr/lib',
    ' --datadir=/usr/share',
    ' --with-png',
    ' --with-xft',
    ' --with-jpeg',
    ' --enable-utf8',
    ' --enable-xrandr',
    ' --enable-xrender',
    ' --enable-xcursor',
    ' --enable-xinerama',
    ' --enable-glw',
    ' --disable-static '
    ])

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure(i)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README.md")
