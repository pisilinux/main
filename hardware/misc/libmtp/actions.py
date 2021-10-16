#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --with-udev=/lib/udev \
                         --with-udev-rules=69-libmtp.rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #install HAL file for portable audio players
    pisitools.insinto("/usr/share/hal/fdi/information/10freedesktop", "libmtp.fdi", "10-usb-music-players-libmtp.fdi")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "AUTHORS", "TODO")
