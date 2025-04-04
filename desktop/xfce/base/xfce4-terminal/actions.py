#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    pisitools.cflags.add("-Wno-deprecated-declarations")
    #autotools.autoreconf("-fiv")
    # shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    mesontools.configure("-Dwayland=enabled")

def build():
    mesontools.build()

def install():
    mesontools.install()
    #pisitools.removeDir("/usr/share/gnome-control-center")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*", "THANKS")

