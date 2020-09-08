#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import mesontools

def setup():
    cmaketools.configure("-Bbuild \
                          -GNinja \
                          -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.dodoc("LICENSE", "README*")