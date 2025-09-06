#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    mesontools.configure("--prefix=/usr \
                          --wrap-mode=default \
                          --sbindir=/usr/bin \
                          --buildtype=plain \
                          --auto-features=enabled \
                          --sysconfdir=/etc \
                          --libexecdir=/usr/lib \
                          -Dudevrulesdir=/lib/udev/rules.d \
                          -D b_lto=true -D b_pie=true \
                          -D docs=man -D docs-build=true \
                          --localstatedir=/var")

def build():
    mesontools.build()

def check():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.domove("/usr/lib/systemd/system/nvmf-connect.target", "/usr/share/dbus-1/services/")
    pisitools.domove("/usr/lib/systemd/system/nvmf-autoconnect.service", "/usr/share/dbus-1/services/")
    pisitools.domove("/usr/lib/systemd/system/nvmefc-boot-connections.service", "/usr/share/dbus-1/services/")
    pisitools.domove("/usr/lib/systemd/system/nvmf-connect@.service", "/usr/share/dbus-1/services/")
    pisitools.domove("/usr/lib/systemd/system/nvmf-connect-nbft.service", "/usr/share/dbus-1/services/")
    pisitools.removeDir("/usr/lib/systemd")

    pisitools.dodoc("LICENSE", "README.md")
