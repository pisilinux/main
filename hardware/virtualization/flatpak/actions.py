#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get


def setup():
    mesontools.configure("-Dselinux_module=disabled \
                          -Dtests=false \
                          -Dsystem_dbus_proxy=xdg-dbus-proxy \
                          -Dsystemd=disabled")


def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.removeDir("/usr/lib/systemd")

    pisitools.dodoc("COPYING", "README*", "NEWS")
