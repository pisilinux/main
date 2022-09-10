#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "-O3", "")
    shelltools.export("CPPFLAGS", get.CXXFLAGS())
    
    shelltools.export("LDFLAGS", "%s -lpthread" % get.LDFLAGS())

    #shelltools.system("./autogen.sh")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-glib \
                         --disable-ecore \
                         --disable-examples")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "COPYING")
