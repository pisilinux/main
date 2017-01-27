#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CC=%s CFLAGS='%s'" % (get.CC(), get.CFLAGS()))

def check():
    autotools.make("-j1 test")

def install():
    pisitools.insinto("/usr/include/", "libjbig/jbig*.h")
    pisitools.insinto("/usr/lib/", "libjbig/libjbig*.so")
    pisitools.insinto("/usr/bin/", "pbmtools/jbgtopbm")
    pisitools.insinto("/usr/bin/", "pbmtools/pbmtojbg")
    pisitools.insinto("/usr/bin/", "pbmtools/jbgtopbm85")
    pisitools.insinto("/usr/bin/", "pbmtools/pbmtojbg85")

    pisitools.doman("pbmtools/jbgtopbm.1", "pbmtools/pbmtojbg.1")
    pisitools.dodoc("ANNOUNCE", "CHANGES", "COPYING", "TODO")
