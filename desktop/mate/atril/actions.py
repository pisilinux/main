#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --libexecdir=/usr/lib \
                         --disable-static \
                         --disable-rpath \
                         --enable-caja \
                         --enable-pdf \
                         --enable-tiff \
                         --enable-djvu \
                         --enable-dvi \
                         --enable-xps \
                         --enable-t1lib \
                         --enable-comics \
                         --enable-pixbuf \
                         --enable-impress \
                         --enable-introspection \
                         --disable-schemas-compile")

    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "AUTHORS", "COPYING")
