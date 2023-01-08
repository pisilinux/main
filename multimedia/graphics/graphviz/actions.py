#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

j = ''.join([
    ' --disable-static',
    ' --without-webp',
    ' --disable-dependency-tracking '
    ])

def setup():
    shelltools.export("LIBPOSTFIX", "/")
    shelltools.export("CONFIG_SHELL", "/bin/bash")
    autotools.configure(j)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
