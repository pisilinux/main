#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2015 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5


def setup():
    #qt5.configure("pgmodeler.pro")
    shelltools.system("qmake -r pgmodeler.pro PREFIX+=/usr BINDIR+=/usr/bin LIBDIR+=/usr/lib RESDIR+=/usr/share")

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.domove("/usr/lib/pgmodeler/lib*", "/usr/lib")

    pisitools.insinto("usr/share/icons/hicolor/64x64/apps", "conf/pgmodeler_logo.png")
    pisitools.dosym("/usr/share/pgmodeler/schemas", "/etc/pgmodeler/schemas")

    pisitools.dodir("/usr/lib/pgmodeler/plugins")

    pisitools.dodoc("LICENSE", "CHANGELOG.md", "README*")
