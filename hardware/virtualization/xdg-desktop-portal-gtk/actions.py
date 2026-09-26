#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Dwallpaper=disabled -Dsystemduserunitdir=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dosed("%s/usr/share/dbus-1/services/*.service" % get.installDIR(), "SystemdService", deleteLine=True)

    portal_conf_dir = "%s/usr/share/xdg-desktop-portal" % get.installDIR()
    shelltools.makedirs(portal_conf_dir)
    
    conf_content = "[preferred]\ndefault=gtk\n"
    shelltools.echo("%s/gtk-portals.conf" % portal_conf_dir, conf_content)

    pisitools.dodoc("COPYING", "NEWS")
