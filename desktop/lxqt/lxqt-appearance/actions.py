#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    pisitools.dosed("data/lxappearance.desktop", "GTK;Settings;DesktopSettings;X-LXDE-Settings;", "Settings;DesktopSettings;Qt;LXQt;")
    pisitools.dosed("data/lxappearance.desktop", "Görünümü Özelleştir", "GTK tema ayarları")
    autotools.configure("--prefix=/usr     \
                                     --sysconfdir=/etc \
                                     --disable-static  \
                                     --enable-dbus \
                                     --enable-gtk3")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING")
