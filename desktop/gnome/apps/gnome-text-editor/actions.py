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
    pisitools.dosed("meson.build", "2.69", "2.68")
    pisitools.dosed("meson.build", "4.3", "4.2")
    pisitools.dosed("meson.build", "5.1.1", "5.1.0")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.dodoc("COPYING", "NEWS", "README*")
