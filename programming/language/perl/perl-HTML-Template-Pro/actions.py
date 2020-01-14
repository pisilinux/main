#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()
    # suppress warning messages
    pisitools.dosed("Makefile", "CCFLAGS = ", "CCFLAGS = -Wno-discarded-qualifiers ")
    # fix runpath analysis
    pisitools.dosed("Makefile", "LD_RUN_PATH=\"\$\(LD_RUN_PATH\)\"", "")

def build():
    perlmodules.make()

def check():
    shelltools.export("LC_ALL", "C")
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("ARTISTIC", "LGPL", "README")