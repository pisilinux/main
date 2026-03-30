#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--with-cli=readline \
                         --disable-debug \
                         --with-json \
                         --disable-python")
    # --with-unitdir=/usr/share/dbus-1/services \

def build():
    autotools.make()

    shelltools.cd("py")
    python3modules.compile()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("py")
    python3modules.install(pyVer="3")

    pisitools.dodoc("../COPYING")
