#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
def setup():
    shelltools.system("./autogen.sh")
    autotools.configure(" \
                         --enable-lcms \
                         --disable-static \
                         --enable-poppler-cairo \
                         --disable-dependency-tracking \
                         --without-gnome-vfs \
                         --without-inkjar \
                         --enable-dbusapi \
                         --enable-nls")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")
