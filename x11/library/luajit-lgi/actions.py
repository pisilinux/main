#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#def setup():
    #autotools.configure()

def build():
    pisitools.dosed("lgi/Makefile", "PREFIX = /usr/local", "PREFIX = /usr")
    autotools.make("LUA_INCDIR=/usr/include/luajit-2.0/ \
                    LUA_CFLAGS='$(pkg-config --cflags luajit) -O2'")

    #autotools.make()

def install():
    autotools.rawInstall("LUA_LIBDIR=/usr/lib/lua/5.3 \
                          LUA_SHAREDIR=/usr/share/lua/5.3 DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
