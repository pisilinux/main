#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Ddbus_service_dir=/usr/share/dbus-1/services \
                          -Dsystemduserunitdir=no \
                         ")
                        #-Dsystemduserunitdir=/usr/lib/systemd/user

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.removeDir("/usr/no")
    pisitools.dosed("%s/usr/share/dbus-1/services/*.service" % get.installDIR(), "SystemdService", deleteLine=True )

    pisitools.dodoc("COPYING", "NEWS", "README*")
