#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "--enable-xorg-libinput \
     --enable-upower-glib \
     --enable-libxklavier \
     --enable-libnotify \
     --enable-gio-unix \
     --enable-xcursor \
     --enable-colord \
     --enable-xrandr \
     --disable-pluggable-dialogs \
     --disable-sound-settings \
     --enable-x11 \
     --enable-wayland \
     --disable-static \
    "

def setup():
    autotools.configure(i)

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")

