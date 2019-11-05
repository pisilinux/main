#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson .. --prefix=/usr \
                                --sysconfdir=/etc \
                                -Dman=false")

    
def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "MAINTAINERS", "COPYING", "RELEASE", "NEWS")
