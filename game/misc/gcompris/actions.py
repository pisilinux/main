#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|gstreamer-0.10|gstreamer-1.0|g' configure")
    shelltools.system("sed -i 's|gstreamer-0.10|gstreamer-1.0|g' configure.ac")
    shelltools.system("sed -i -e 's/$GNUCHESS/gcompris-gnuchess/' configure")
    
    shelltools.export("LDFLAGS", "%s -lgmodule-2.0" % get.LDFLAGS())
    autotools.configure("--prefix=/usr --enable-py-build-only")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "INSTALL")
