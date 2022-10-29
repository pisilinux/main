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
    shelltools.cd("subprojects/appmenu-gtk-module")
    mesontools.configure()

def build():
    shelltools.cd("subprojects/appmenu-gtk-module")
    mesontools.build()

def install():
    shelltools.cd("subprojects/appmenu-gtk-module")
    mesontools.install()
    
    # pisitools.dodoc("LICENSE", "README*")
