#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("meson.build", "datadir", "libdir")
    #autotools.configure()

def build():
    shelltools.system("meson build --libdir=/usr/lib --includedir=/usr/include/EGL")

def install():
    mesontools.install()
    # pisitools.insinto("/usr/include/EGL", "interface/*")
    # pisitools.insinto("/usr/lib/pkgconfig", "*.pc")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README*")
