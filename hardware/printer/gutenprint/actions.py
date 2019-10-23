#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #shelltools.system("sed -i 's:cups_sbindir=\"\/usr\/sbin\":cups_sbindir=\"\/usr\/bin\":g' m4/stp_cups.m4")
    #shelltools.system("sed -i  's:cups_sbindir=\"\${cups_prefix}\/sbin\":cups_sbindir=\"\${cups_prefix}\/bin\":' m4/stp_cups.m4")  
    shelltools.system("sed -i 's:m4local:m4extra:' Makefile.am")

    autotools.autoreconf("-fi")

    autotools.configure("--prefix=/usr \
                         --sbindir=/usr/bin \
                         --enable-samples \
                         --enable-cups-ppds \
                         --enable-cups-ppds-at-top-level \
                         --disable-translated-cups-ppds \
                         --disable-globalized-cups-ppds \
                         --disable-static \
                         --disable-static-genppd")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())
