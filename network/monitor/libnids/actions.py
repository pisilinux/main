#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-unused-result -Wno-deprecated-declarations")
    #shelltools.export("CFLAGS", "-Wno-unused-result -Wno-deprecated-declarations")
    # Fix soname
    pisitools.dosed("src/Makefile.in", "^LIBSHARED.*", "LIBSHARED = libnids.so.%s" % get.srcVERSION().split(".", 1)[0])

    # disable static
    pisitools.dosed("src/Makefile.in", "\$\(INSTALL.*libnids.a.*")

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("install_prefix=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "MISC", "README", "doc/*")