#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "AM_CONFIG_HEADER", "AC_CONFIG_HEADERS")
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --disable-example-progs \
                         --enable-cpp-progs \
                         --with-cd-paranoia-name=libcdio-paranoia")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % (get.installDIR()))

    pisitools.dodoc("AUTHORS", "NEWS.md", "THANKS")
