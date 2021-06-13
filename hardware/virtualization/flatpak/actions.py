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
    autotools.autoreconf("-fiv")
    autotools.configure("--enable-selinux-module=no \
                         --with-system-bubblewrap \
                         --with-priv-mode=none \
                         --with-system-dbus-proxy \
                         --without-systemd")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # shelltools.system('install -d -o root -g 102 -m 750 "%s/usr/share/polkit-1/rules.d"' % get.installDIR())

    pisitools.removeDir("/usr/lib/systemd")

    pisitools.dodoc("COPYING", "README*", "NEWS")
