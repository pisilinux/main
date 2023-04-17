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
    mesontools.configure("-Dlibnma_gtk4=true")

def build():
    mesontools.build()

def install():
    mesontools.install()

    # network-manager-applet 1.32.0
    pisitools.remove("/usr/share/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml")
    
    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")
