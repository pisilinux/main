#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--enable-reentrant \
     --enable-libical \
     --with-bdb4 \
     --disable-static \
    "

i = "-Wno-deprecated-declarations \
     -Wno-implicit-function-declaration \
     -Wno-stringop-overflow \
    "

def setup():
    pisitools.cflags.add(i)
    autotools.configure(j)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")

