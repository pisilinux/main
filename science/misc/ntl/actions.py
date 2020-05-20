#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("src")
    autotools.rawConfigure("DEF_PREFIX=/usr SHARED=on NTL_GF2X_LIB=on NATIVE=off TUNE=x86 LIBTOOL=libtool")

def build():
    shelltools.cd("src")
    autotools.make()

def check():
    shelltools.cd("src")
    autotools.make("-k check")

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dodoc("README")