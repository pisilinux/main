#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools


def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.autoreconf("-vfi")
    autotools.automake("-afc")
    libtools.libtoolize("--automake")
    autotools.aclocal()
    autotools.autoconf()
    autotools.configure("--disable-static --enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/lib/pkgconfig")
    pisitools.dodoc("COPYING*", "README")
