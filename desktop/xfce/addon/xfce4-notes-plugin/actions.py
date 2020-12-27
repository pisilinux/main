#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "-Wno-incompatible-pointer-types -Wno-implicit-function-declaration -Wno-deprecated-declarations"

def setup():
    pisitools.cflags.add(i)
    shelltools.system("./autogen.sh --prefix=/usr \
                                    --sysconfdir=/etc \
                                    --libexecdir=/usr/lib \
                                    --localstatedir=/var \
                                    --disable-static \
                                    --disable-dependency-tracking \
                                    --host=%s \
                                    --disable-debug" % get.CHOST())

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")

