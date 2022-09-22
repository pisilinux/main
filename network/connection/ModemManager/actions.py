#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Dvapi=true \
                          -Dgtk_doc=true \
                          -Dpolkit=permissive \
                          -Dsystemd_journal=false \
                          -Dsystemdsystemunitdir=no \
                          -Dat_command_via_dbus=true \
                          -Ddbus_policy_dir=/usr/share/dbus-1/system.d \
                          ")

def build():
    mesontools.build()

# def check():
     # mesontools.build("test")

def install():
    mesontools.install()

    pisitools.dosed("%s/usr/share/dbus-1/system-services/*.service" % get.installDIR(), "SystemdService", deleteLine=True )

    pisitools.dodoc("README", "COPYING")
