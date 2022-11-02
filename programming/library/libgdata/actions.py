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
    # pisitools.dosed("meson.build", "gcr-base-3", "gcr-4")
    # pisitools.dosed("gdata/gdata-service.c", "gcr-base.h", "gcr.h")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
