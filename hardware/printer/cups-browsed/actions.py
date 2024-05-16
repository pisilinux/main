#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--localstatedir=/var \
                         --with-rcdir=no \
                         --enable-auto-setup-driverless-only")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/dbus-1/services", "daemon/cups-browsed.service")

    pisitools.dodoc("AUTHORS", "LICENSE", "ChangeLog", "COPYING", "NEWS", "README*")
