#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system(""" sed -i -r 's:"(/system):"/org/gnome\1:g' src/external.gschema.xml""")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.removeDir("/usr/lib/systemd")

    pisitools.dodoc("COPYING*", "README*")
