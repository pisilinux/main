#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get


def setup():
    # shelltools.system("env NOCONFIGURE=1 ./autogen.sh")
    
    mesontools.configure("--buildtype=release \
                          -Dtests=false \
                          -Dselinux=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("README*", "COPYING")
