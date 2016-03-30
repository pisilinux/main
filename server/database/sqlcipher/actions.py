#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -DSQLITE_HAS_CODEC -DSQLITE_TEMP_STORE=2" % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -lcrypto" % get.LDFLAGS())
    autotools.configure("--prefix=/usr \
                         --enable-tempstore=yes \
                         --enable-readline \
                         --enable-threadsafe \
                         --enable-cross-thread-connections \
                         --enable-releasemode \
                         --disable-static \
                         --with-crypto-lib")
    
    #for unused
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG*", "README*", "VERSION", "LICENSE")
