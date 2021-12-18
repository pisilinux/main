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
    shelltools.system("meson --prefix=/usr \
                                -Dlogind=false \
                                -Dnfs=false \
                                -Dgoa=true \
                                -Dman=true \
                                -Dgoogle=true \
                                -Dtmpfilesdir=no \
                                -Dsystemduserunitdir=no ..")
    
def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    
def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("COPYING*", "NEWS*", "README*")
