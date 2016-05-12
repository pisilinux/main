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
    shelltools.export("AUTOPOINT", "true")
    shelltools.export("NOCONFIGURE", "1")
    shelltools.system("./autogen.sh")
    autotools.autoreconf("-vi")

    autotools.configure("--disable-static \
                         --disable-experimental \
                         --with-package-name='PisiLinux gstreamer-plugins-bad package' \
                         --with-package-origin='http://www.pisilinux.org' \
                         --with-gtk=3.0")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ") 

def build():
    autotools.make()

#FIXME: tests now tries to 
#def check():
#    # for sandbox violations
#    autotools.make("-C tests/check check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "RELEASE", "REQUIREMENTS")