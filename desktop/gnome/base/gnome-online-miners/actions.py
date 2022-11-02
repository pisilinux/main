#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#
# TODO: Add libzapojit (Hotmail&Skydrive) support.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("TRACKER_LIBS","-ltracker-sparql-3.0")
    shelltools.export("TRACKER_CFLAGS","-I/usr/include/tracker-3.0")

    autotools.autoreconf("-fi")
    autotools.configure("--disable-silent-rules \
                         --disable-static \
                         --without-gfbgraph \
                         --disable-windows-live")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README")
