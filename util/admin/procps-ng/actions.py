#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's:<ncursesw/:<:g' -i watch.c")
    autotools.autoreconf("-vif")
    autotools.configure("--enable-watch8bit \
                         --without-systemd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "AUTHORS", "NEWS")

    pisitools.remove("/usr/bin/kill")
    pisitools.remove("/usr/share/man/man1/kill.1")