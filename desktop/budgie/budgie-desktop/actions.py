#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure(
        "--libexecdir=/usr/lib "
        "-Dbudgie-session-libexecdir=/usr/lib/budgie-session "
        "-Dgsd-libexecdir=/usr/lib/gnome-settings-daemon "
        "-Dxdp-libexecdir=/usr/lib/xdg-desktop-portal "
        "-Dwith-runtime-dependencies=false"
    )

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.dodoc("LICENSE")