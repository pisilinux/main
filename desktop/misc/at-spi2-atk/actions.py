#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "meson --prefix=/usr --sysconfdir=/etc \
              "
                     
    if get.buildTYPE() == "emul32":
        options += "--libdir=lib32 .."
                
    shelltools.system(options)

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    if get.buildTYPE() == "emul32":
        return
    
        shelltools.cd("build")
        pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS")
