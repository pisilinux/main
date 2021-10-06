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
    mesontools.configure("-D ipv6=true \
                            -D glx=true \
                            -D dpms=true \
                            -D xace=true \
                            -D xvfb=true \
                            -D xdmcp=true \
                            -D xinerama=true \
                            -D xcsecurity=true \
                            -D screensaver=true \
                            -D dri3=true \
                            -D xwayland_eglstream=true \
                            -D glamor=true \
                            -D xkb_dir=/usr/share/X11/xkb \
                            -D xkb_output_dir=/var/lib/xkb")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.dodoc("COPYING", "README*")
