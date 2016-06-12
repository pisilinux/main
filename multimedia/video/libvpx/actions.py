#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

libdir = "lib"

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --libdir=/usr/%s \
                            --enable-pic \
                            --enable-vp8 \
                            --enable-vp9 \
                            --enable-vp9-highbitdepth \
                            --enable-shared \
                            --enable-runtime-cpu-detect \
                            --enable-postproc \
                            --enable-experimental \
                            --enable-spatial-svc \
                            --disable-install-docs \
                            --disable-install-srcs" % libdir)


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/%s/*.a" % libdir)

    pisitools.dodoc("AUTHORS", "CHANGELOG", "LICENSE", "PATENTS")
