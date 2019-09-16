#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.system("sed -i 's|$(datadir)/pkgconfig|$(libdir)/pkgconfig|g' Makefile.in")
    #shelltools.system("sed -i 's|$(datadir)/pkgconfig|$(libdir)/pkgconfig|g' Makefile.am")
    #pisitools.dosed("Makefile.in", "pkgconfigdir = $(datadir)/pkgconfig", "pkgconfigdir = $(libdir)/pkgconfig")
    #pisitools.dosed("Makefile.am", "pkgconfigdir = $(datadir)/pkgconfig", "pkgconfigdir = $(libdir)/pkgconfig")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.copytree("%s/usr/share/pkgconfig" % get.installDIR(), "%s/usr/lib/pkgconfig" % get.installDIR())
    pisitools.removeDir("/usr/share/pkgconfig")
    
    pisitools.dodoc("AUTHORS", "NEWS", "COPYING*")
