#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("data/configs/*.service.in", "SystemdService", deleteLine=True)
    autotools.configure("--disable-static \
                         --sysconfdir=/etc \
                         --disable-schemas-compile \
                         --with-dhcp-config='/etc/dhcp/dhcpd.conf' \
                         --with-systemduserunitdir=no \
                         --with-systemdsystemunitdir=no \
                         --enable-pulseaudio \
                         --enable-polkit")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chmod(get.installDIR() + "/usr/share/polkit-1/rules.d")

    pisitools.dodoc("CHANGELOG.*", "COPYING")
