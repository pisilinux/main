#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

def setup():
    # fix build failure w/ xfce4-panel-4.15.0
    #pisitools.dosed("src/smartbookmark.c", "<libxfce4panel/xfce-panel-plugin.h>", "<libxfce4panel/libxfce4panel.h>")
    autotools.configure()

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS")
