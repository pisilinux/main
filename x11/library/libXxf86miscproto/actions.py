# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #FIXME:Remove files which conflict with xorg-proto
    #pisitools.remove("/usr/include/X11/extensions/xf86mscstr.h")
    #pisitools.remove("/usr/include/X11/extensions/xf86misc.h")
    #pisitools.remove("/usr/lib/pkgconfig/xf86miscproto.pc")

    pisitools.dodoc("ChangeLog", "COPYING")
