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
    shelltools.export("PYTHON", "/usr/bin/python3")
    pisitools.dosed("configure", "-Werror", "")
    autotools.configure("--disable-static \
                         --libexecdir=/usr/lib \
                         --sysconfdir=/etc \
                         --enable-gtk-doc-html=no \
                         --enable-gtk-doc")

    pisitools.dosed("libtool"," -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README","NEWS")
