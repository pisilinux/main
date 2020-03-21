#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

w = "-Wno-unused-but-set-variable -Wno-deprecated-declarations \
-Wno-incompatible-pointer-types -Wno-multichar -Wno-unused-result \
-Wno-misleading-indentation -Wno-dangling-else -Wno-parentheses \
-Wno-unused-variable -Wno-unused-value -Wno-vla"

def setup():
    pisitools.cflags.add(w)
    autotools.configure("--disable-oss")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README")

