#!/usr/bin/python
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
    # shelltools.system("sed -i -e 's:AM_CONFIG_HEADER:AC_CONFIG_HEADERS:' configure.ac")
    # shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    mesontools.configure("--prefix=/usr --sysconfdir=/etc")

def build():
    # mesontools.build("-C po update-gmo")
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")
