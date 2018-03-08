#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson .. --prefix=/usr \
                                --sysconfdir=/etc \
                                -Dwith-daemon-user=colord \
                                -Denable-systemd=false \
                                -Denable-docs=false \
                                -Denable-man=false")

    
def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    pisitools.insinto("/etc/dbus-1/system.d/","%s/usr/share/dbus-1/system.d/org.freedesktop.ColorManager.conf" % get.installDIR())
    pisitools.removeDir("/usr/share/dbus-1/system.d")

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "MAINTAINERS", "COPYING", "RELEASE", "NEWS", "README.md")
