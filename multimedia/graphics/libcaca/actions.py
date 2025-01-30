#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-doc \
                         --disable-static \
                         --disable-ruby \
                         --disable-csharp \
                         --disable-java \
                         --disable-cxx \
                         --disable-gl \
                         --enable-shared \
                         --enable-ncurses \
                         --enable-slang \
                         --enable-imlib2 \
                         --enable-x11 \
                         --with-x \
                         --x-libraries=/usr/lib")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "THANKS")
