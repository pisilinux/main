#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools, shelltools, get

def setup():
    mesontools.configure("--prefix=/usr --buildtype=plain")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.domove("/usr/lib/systemd/user/cpupower-gui-user.service", "/usr/share/dbus-1/services/")
    pisitools.domove("/usr/lib/systemd/system/cpupower-gui-helper.service", "/usr/share/dbus-1/services/")
    pisitools.domove("/usr/lib/systemd/system/cpupower-gui.service", "/usr/share/dbus-1/services/")

    pisitools.removeDir("/usr/lib/systemd")

    pisitools.dodoc("COPYING", "README.md")
