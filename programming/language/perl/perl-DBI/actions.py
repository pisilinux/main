#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    # suppress compiler warnings
    pisitools.dosed("Makefile.PL", "-Wno-comment", "-Wno-comment -Wno-cast-function-type")
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("LICENSE", "MANIFEST", "README*")