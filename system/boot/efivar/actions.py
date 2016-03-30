#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", "-Os")
    pisitools.dosed("Make.defaults","-O0","-Os")
    pisitools.dosed("src/test/Makefile","-rpath=$(TOPDIR)/src/","-rpath=$(libdir)|g")
    autotools.make("libdir=/usr/lib bindir=/usr/bin includedir=/usr/include/ V=1 -j1")

def install():
     autotools.rawInstall("DESTDIR=%s libdir=/usr/lib/" % get.installDIR())
