#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Net-SSLeay-%s" % get.srcVERSION()

def setup():
    perlmodules.configure("-- /usr/include/openssl/")
    # suppress warnings
    pisitools.dosed("Makefile","CCFLAGS =","CCFLAGS = -Wno-deprecated-declarations -Wno-discarded-qualifiers")
    # fix unused direct dependency analysis
    pisitools.dosed("Makefile","LDDLFLAGS =","LDDLFLAGS = -Wl,-O1,--as-needed")
    # fix runpath analysis
    pisitools.dosed("Makefile","LD_RUN_PATH=\"\$\(LD_RUN_PATH\)\"", "")

def build():
    perlmodules.make()

#def check():
    #perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("LICENSE","README")
