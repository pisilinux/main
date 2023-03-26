#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-twinserial \
                         --enable-serialconfdir=/etc/reader.conf.d \
                         --sysconfdir=/etc \
                         --disable-static \
                         --disable-dependency-tracking")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/etc/", "src/Info.plist", "libccid_Info.plist")

    pisitools.insinto("/etc/udev/rules.d/", "src/92_pcscd_ccid.rules", "92-pcsc-ccid.rules")
    pisitools.dosed("%s/etc/udev/rules.d/92-pcsc-ccid.rules" % get.installDIR(), "Kobil_mIDentity_switch", deleteLine = True)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
