#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.export("PYTHON", "/usr/bin/python3.6")
    autotools.configure("--sysconfdir=/etc \
                         --enable-drm \
                         --enable-geoclue2 \
                         --enable-randr \
                         --enable-vidmode \
                         --with-systemduserunitdir=/usr/lib/systemd/user")
    
    
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    #autotools.install()
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CONTRIB*", "COPYING", "README*")
