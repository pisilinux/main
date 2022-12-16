#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

pisitools.cflags.add("-Wno-deprecated-declarations")

def setup():
    autotools.configure("--enable-dbus-start-daemon \
    --enable-old-get-server-information-signature \
    --enable-old-notification-closed-signature")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("usr/lib/systemd")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")

