#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure", "rest-0.7", "rest-1.0")
    pisitools.dosed("configure.ac", "rest-0.7", "rest-1.0")
    pisitools.dosed("Makefile.am", "rest-0.7", "rest-1.0")
    pisitools.dosed("Makefile.in", "rest-0.7", "rest-1.0")

    shelltools.export("GFBGRAPH_LIBS","-ltracker-sparql-3.0")
    shelltools.export("TRACKER_LIBS","-ltracker-sparql-3.0")
    shelltools.export("TRACKER_LIBS","-ltracker-sparql-3.0")
    shelltools.export("TRACKER_LIBS","-ltracker-sparql-3.0")

    # pisitools.dosed("configure", "libsoup-2.4", "libsoup-3.0")
    # pisitools.dosed("configure.ac", "libsoup-2.4", "libsoup-3.0")
    # pisitools.dosed("Makefile.am", "libsoup-2.4", "libsoup-3.0")
    # pisitools.dosed("Makefile.in", "libsoup-2.4", "libsoup-3.0")

    autotools.autoreconf("-fiv")

    autotools.configure("--enable-introspection")
    
    
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.removeDir("/usr/doc")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
