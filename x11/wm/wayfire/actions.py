#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Duse_system_wfconfig=enabled \
                          -Duse_system_wlroots=enabled \
                          -Dxwayland=enabled \
                          --auto-features=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.insinto("/usr/share/doc/wayfire/examples", "wayfire.ini")
    
    #shelltools.cd("..")
    pisitools.dodoc("LICENSE", "README*")
