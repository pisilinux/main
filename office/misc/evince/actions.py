#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # pisitools.dosed("meson.build", "3.28.0", "43.0")
    # pisitools.dosed("meson.build", "42.20", "43.20")
    #shelltools.system("sed -i -e 's:T1_initLib:T1_InitLib:' meson.build || die")
    mesontools.configure("-Dps=enabled -Ddvi=disabled \
                          -Dsystemduserunitdir=no \
                          -Dplatform=gnome")

def build():
    mesontools.build()
    
def install():
    mesontools.install()
    
    pisitools.dodoc("AUTHORS", "NEWS*", "README*", "COPYING", "TODO")
