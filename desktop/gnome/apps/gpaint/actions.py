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
    shelltools.system("""sed -i 's#GTK_RESPONSE_DISCARD#GTK_RESPONSE_NO#' src/drawing.c""")

def build():
    autotools.configure(" --prefix=/usr")
    autotools.make("LDFLAGS+=-lm")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())  
    pisitools.insinto("/usr/bin/","src/gpaint-2", "gpaint")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "NEWS", "README", "THANKS", "TODO")
    shelltools.cd("%s/usr/" % get.installDIR())
    shelltools.system("rm -rf bin/gpaint-2")
    shelltools.system("rm -rf share/applications/gpaint.desktop")

