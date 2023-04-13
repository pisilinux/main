#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get


def setup():
    mesontools.configure("--localstatedir=/var \
                                -Delogind=enabled \
                                -Dsystemd=disabled \
                                -Dconsolekit=disabled \
                                -Ddocs=disabled \
                                -Dman=false")

def build():
    mesontools.build()
    

def install():
    mesontools.install()
    
    pisitools.dodoc("COPYING", "README*")
