#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure()

def build():
    mesontools.build()

def install():
    shelltools.copy("COPYING", "LICENSE")
    mesontools.install()
    pisitools.dodoc("LICENSE", "README*")
