#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    # fix build failure w/ xfce4-panel-4.15.0
    pisitools.dosed("panel-plugin/devices.c", "<libxfce4panel/xfce-panel-plugin.h>", "<libxfce4panel/libxfce4panel.h>")
#    pisitools.dosed("panel-plugin/mount-plugin.h", "<libxfce4panel/xfce-panel-plugin.h>", "<libxfce4panel/libxfce4panel.h>")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")

