#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    options = "--disable-static \
               --disable-sqlite \
               --enable-flac \
               --enable-alsa \
               --enable-largefile \
               --disable-gcc-pipe \
               --disable-jack \
               --disable-octave \
               --disable-gcc-werror \
               --disable-dependency-tracking"

    shelltools.unlink("M4/libtool.m4")

    for i in shelltools.ls("M4/lt*.m4"):
        shelltools.unlink(i)

    pisitools.cflags.add("-Wno-expansion-to-defined -Wno-format-truncation -Wno-implicit-fallthrough")
    autotools.autoreconf("-fi -I M4")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")