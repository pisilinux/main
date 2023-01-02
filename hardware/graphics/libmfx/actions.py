#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

i = ''.join([
    ' --with-libva_drm=yes',
    ' --with-libva_x11=yes',
    ' --enable-shared',
    ' --disable-static '
    ])

def setup():
	autotools.autoreconf("-vfi")
	autotools.configure(i)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
