#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-Wno-unused-but-set-variable \
     -Wno-unused-result \
     -Wno-deprecated-declarations \
     -Wno-stringop-truncation \
    "

def setup():
    # suppress compiler warnings
    pisitools.cflags.add(j)
    shelltools.export("OPTIMIZER", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.configure("--sbindir=/usr/sbin --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DIST_ROOT="%s"' % get.installDIR())
