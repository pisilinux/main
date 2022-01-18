#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' --enable-lefty',
    ' --disable-r',
    ' --disable-lua',
    ' --disable-php',
    ' --disable-rpath',
    ' --disable-static',
    ' --disable-dependency-tracking',
    ' --with-libgd',
    ' --with-fontconfig',
    ' --with-pangocairo',
    ' --without-webp',
    ' --without-devil '
    ])

def setup():
    shelltools.export("LIBPOSTFIX", "/")
    shelltools.export("CONFIG_SHELL", "/bin/bash")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure(j)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
