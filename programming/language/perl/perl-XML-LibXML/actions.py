#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()
    # suppress warning messages
    pisitools.dosed("Makefile", "CCFLAGS = ", "CCFLAGS = -Wno-stringop-overflow -Wno-incompatible-pointer-types ")
    # fix unused direct dependency analysis
    pisitools.dosed("Makefile","LDDLFLAGS =","LDDLFLAGS = -Wl,-O1,--as-needed")
    # fix runpath analysis
    pisitools.dosed("Makefile","LD_RUN_PATH=\"\$\(LD_RUN_PATH\)\"", "")

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("README", "LICENSE", "Changes")