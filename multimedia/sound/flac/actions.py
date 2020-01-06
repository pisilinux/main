#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    options  = "--with-pic \
                --enable-ogg \
                --enable-sse \
                --disable-doxygen-docs \
                --disable-dependency-tracking \
                --disable-xmms-plugin \
                --disable-static"
    pisitools.cflags.add("-Wno-stringop-overflow -Wno-stringop-truncation")
    autotools.autoconf()
    autotools.configure(options)
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README*")