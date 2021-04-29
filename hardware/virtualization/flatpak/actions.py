#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure(" --enable-selinux-module=no \
                          --with-system-bubblewrap \
                          --disable-static \
                          --with-priv-mode=setuid \
                          --with-profile-dir=/etc/profile.d \
                          --with-dbus-config-dir=/usr/share/dbus-1/system.d \
                          --disable-nls")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/lib/systemd")

    pisitools.dodoc("COPYING", "README*", "NEWS")
