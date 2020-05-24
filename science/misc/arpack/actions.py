#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#shelltools.export("OMPI_ALLOW_RUN_AS_ROOT", "1")
shelltools.export("PKG_CONFIG_PATH", "/usr/lib/openmpi/pkgconfig")

def setup():
    autotools.autoreconf("-vif")
    shelltools.export("LDFLAGS", "-L/usr/lib/openmpi")
    autotools.configure("--enable-mpi --enable-icb")

    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("F77='mpif77' \
                    CFLAGS+=' `pkg-config --cflags ompi-f77` ' \
                    LIBS+=' `pkg-config --libs ompi-f77`' ")

# run as root failure
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "README*")