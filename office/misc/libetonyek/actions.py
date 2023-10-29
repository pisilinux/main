#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.cxxflags.add("-std=gnu++11")
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --disable-werror \
                         --without-docs \
                         --enable-static=no \
                         --with-mdds=2.0")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "FEATURES")
