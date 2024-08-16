#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# def setup():
    # shelltools.export("LDFLAGS", "%s" % get.LDFLAGS())
    # autotools.configure()

def build():
    autotools.make('PREFIX=/usr PCDIR=/usr/lib/pkgconfig LDFLAGS="%s"' % get.LDFLAGS())

def install():
    autotools.rawInstall("PREFIX=/usr PCDIR=/usr/lib/pkgconfig DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README*")
