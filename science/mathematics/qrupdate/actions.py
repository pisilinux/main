#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("Makeconf", "FFLAGS=-fimplicit-none -O3 -funroll-loops ", "FFLAGS=%s %s" % (get.CFLAGS(), get.LDFLAGS()))

def build():
    autotools.make("PREFIX=/usr solib")

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "README*")