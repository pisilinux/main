#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.sym("patches/acconfig.h", "acconfig.h")

    autotools.autoreconf("-vfi")
    pisitools.dosed("src/Makefile.in", "@LIBWMF_GDK_PIXBUF_TRUE@", "#")
    autotools.configure("--without-expat \
                         --with-libxml2 \
                         --with-jpeg \
                         --with-x \
                         --with-fontdir=/usr/share/libwmf/fonts \
                         --disable-static")
def build():
    autotools.make("LIBTOOL=/usr/bin/libtool")

def install():
    autotools.rawInstall("DESTDIR=%s \
                          fontdir=/usr/share/libwmf/fonts" % get.installDIR())

    pisitools.dodoc("CREDITS", "COPYING", "README")
    pisitools.remove("/usr/lib/*.a")
