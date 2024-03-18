#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    # shelltools.system("sh ./autogen.sh")
    # autotools.configure()
    mesontools.configure()

def build():
    # autotools.make()
    mesontools.build()

def install():
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
