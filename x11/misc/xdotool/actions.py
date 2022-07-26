#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#def setup():
    #autotools.configure()

prefix = "/usr"
libdir = "/usr/lib"
mandir = "/usr/share/man"

def build():
    pisitools.dosed("Makefile", "/usr/local", "/usr")
    pisitools.dosed("libxdo.pc", "local/", "")

    autotools.make("WITHOUT_RPATH_FIX=1")

def install():
    autotools.install("DESTDIR=%s PREFIX=/usr INSTALLLIB=/usr/lib INSTALLMAN=/usr/share/man" %  get.installDIR())
    #autotools.install("DESTDIR=%s PREFIX=%s INSTALLLIB=%s INSTALLMAN=%s" % ( get.installDIR(), prefix, libdir, mandir))


    pisitools.dodoc("CHANGELIST")
