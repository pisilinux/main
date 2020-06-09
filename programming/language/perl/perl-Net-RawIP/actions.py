#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-implicit-function-declaration -Wno-deprecated-declarations -Wno-cpp")
    perlmodules.configure()
    # fix runpath analysis
    pisitools.dosed("Makefile","LD_RUN_PATH=\"\$\(LD_RUN_PATH\)\"", "")

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("MANIFEST", "README*")