#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = ''.join([
    ' --enable-hdr-subdir',
    ' --enable-pc-files',
    ' --with-Xaw3d{,xft}',
    ' --with-shared '
    ])

def setup():
    autotools.configure(i)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES")

