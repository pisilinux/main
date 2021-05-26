#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --sbindir=/usr/bin")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "CONTRIBUTING", "COPYING", "ChangeLog", "INSTALL", "NEWS", "README*")