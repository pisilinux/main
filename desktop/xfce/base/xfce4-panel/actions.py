#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "--enable-introspection  \
     --enable-gtk-doc  \
     --enable-gio-unix  \
     --enable-vala=yes \
     --disable-debug  \
     --disable-static \
    "

def setup():
    pisitools.cflags.add("-Wno-deprecated-declarations")
    # windowmenu plugin: list width.
    pisitools.dosed("plugins/windowmenu/windowmenu.c", "24", "300")
    autotools.configure(i)

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #fixed whisker menu
    pisitools.dosed("%s/etc/xdg/xfce4/panel/default.xml" % get.installDIR(), "applicationsmenu", "whiskermenu")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS*")
