#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt
# TODO: glade catalog fails the build, needs to be fixed
# (it is probably because of some missing dependencies on a fresh install ??gladeui??)

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("-Dglade_catalog=disabled")

def build():
    mesontools.build

def install():
    mesontools.install()
    pisitools.dodoc("AUTHORS", "COPYING", "HACKING.md", "README.md")
