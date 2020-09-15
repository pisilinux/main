#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

i = "-Wno-deprecated-declarations \
     -Wno-incompatible-pointer-types \
     -Wno-implicit-function-declaration"

def setup():
    # suppress compiler warnings
    pisitools.cflags.add(i)
    autotools.configure()

    # fix unused direct dependency analysis
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")