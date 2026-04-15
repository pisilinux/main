#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "build/linux"

y = ''.join([
    ' --prefix=/usr',
    ' --extra-ldflags="-Wl,-z,noexecstack"',
    ' --extra-cflags="-Wno-incompatible-pointer-types -Wno-implicit-function-declaration"',
    ' --chroma-format="all"',
    ' --enable-pic',
    ' --enable-shared',
#    ' --disable-asm',
    ' --disable-avs',
    ' --disable-swscale',
    ' --disable-lavf',
    ' --disable-ffms',
    ' --disable-gpac',
    ' --disable-lsmash '
    ])

def setup():
    autotools.rawConfigure(y)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), argument = 'install-{cli,lib-shared}')

    pisitools.dodoc("../../COPYING")
